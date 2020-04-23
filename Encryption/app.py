from Encryption.Monoalpha import Monoalpha
from Encryption.CesarEncryption import CesarEncryption
from Encryption.database.databaseMethods import connet_to_database , check_existing_users


class MenuClass:
  def __login__(self):

    print("Login")
    username = input("Enter your name: ")
    connet_to_database()

    user = check_existing_users(username)
    print("Welcome " + str(user))

    return username


  def menu(self, user_name):

    print(
      " 1. Cesarverschlüsselung starten \n 2. Monoalphabetische Substition starten \n 3. Impressum/About \n 4. Programm beenden \n ")

    while True:

      choice = input("chose a number:")
      if choice == "1":
        CesarEncryption(user_name)
        self.menu(user_name)
      if choice == "2":
        Monoalpha(user_name)
        self.menu(user_name)
      if choice == "3":
        print(
          " \n Impressum/About: \n Übung 3 \n Code von Majdi und Kira \n ------------------------------------------------------------- \n ")
        self.menu(user_name)
      if choice == "4":
        print("See you later ")
        exit()
      else:

        print("invalid command, please choose a number between 1 and 4 :)")
        self.menu(user_name)



if __name__ == '__main__':
  first = MenuClass()
  username = first.__login__()
  first.menu(username)







