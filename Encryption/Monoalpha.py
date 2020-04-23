import string
from Encryption.database.databaseMethods import add_encrypted_string, add_mono

ListOfCharacters = string.ascii_uppercase + string.digits + string.punctuation + string.ascii_lowercase
class Monoalpha:

  def __init__(self, username):
    add_mono()
    user_input = input("write something: ")
    result = monoEncryption(user_input)
    add_encrypted_string(result, username)
    print(result)


def monoEncryption(user_input):
  encrypted_msg = ""
  for i in range(len(user_input)):
    char = user_input[i]
    if char in ListOfCharacters:
      location = ListOfCharacters.find(char)
      size = len(ListOfCharacters)
      new_location = size-location
      value = ListOfCharacters[new_location-1]
      encrypted_msg += value
    else:
      encrypted_msg += " "
  return encrypted_msg







