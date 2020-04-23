from Encryption.database.databaseMethods import add_cesar , add_encrypted_string
import random
import string

ListOfCharacters = string.ascii_uppercase + string.digits + string.punctuation + string.ascii_lowercase
class CesarEncryption:

  def __init__(self, userName):

    shift = input("Please enter the value of the offset: ")
    if shift == "":
      print("a random offset value will be chosen for you : ")
      shift = random.randint(0, 1024)
      add_cesar(int(shift))
    else:
      add_cesar(int(shift))

    user_input = input("write something: ")

    result = encoding(shift, user_input)

    add_encrypted_string(result, userName)
    print(result)


def encoding(shift, user_input):
  global encrypted_msg

  encrypted_msg = ""
  for i in range(len(user_input)):
      char = user_input[i]
      if char in ListOfCharacters:
          location = ListOfCharacters.find(char)  # the method find() search in the listofcharacters for a letter or number.
          new_location = ((location + int(shift)) % 94)
          encrypted_msg += ListOfCharacters[new_location]
      else:
          encrypted_msg += " "

  return encrypted_msg








