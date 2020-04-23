from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


SqlAlchemyBase = declarative_base()

class User(SqlAlchemyBase):

  __tablename__ = 'user'

  someid = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(100), nullable=False, unique=True)
  user_password = Column(String, nullable=True) # password is only used in Flask app, here in the console it will always be passed as None
  #Create a relationship to the EncryptedString Table
  encryptedStrings = relationship("EncryptedString", back_populates="user")

  def __init__(self, name: str, password: str = None):
    self.name = name
    self.user_password = password
    

  def __repr__(self):
    return "User [ID: {0}, name: {1}, password:{2} ]".format(self.someid, self.name, self.user_password)


class EncryptedString(SqlAlchemyBase):

  __tablename__ = 'encrypted_string'

  id = Column(Integer, primary_key=True, autoincrement=True)
  string = Column(String, nullable=False)
  #Creates a relationship to the User Table
  user_id = Column(Integer, ForeignKey("user.someid"), nullable=False)
  user = relationship("User", back_populates="encryptedStrings")
  # Creates a relationship to the EncryptionType Table
  encryption_type_id = Column(Integer, ForeignKey("encryption_type.encryptionType_id"), nullable=False)
  encryption_types = relationship("EncryptionType", back_populates="encryptedStrings")

  def __init__(self, string: str, user_id: int, encryption_type_id: int):
    self.string = string
    self.user_id = user_id
    self.encryption_type_id = encryption_type_id

  def __repr__(self):
    return "Encrypted String [id: {0} , string: {1} , user_id: {2} , encryption_type_id {3]".format(self.id, self.string, self.user_id, self.encryption_type_id)


class EncryptionType(SqlAlchemyBase):

  __tablename__ = "encryption_type"

  encryptionType_id = Column(Integer, primary_key=True, autoincrement=True)
  encryption_type = Column(String, nullable=False)
  # Creates a relationship to the EncryptionString Table
  encryptedStrings = relationship("EncryptedString", back_populates="encryption_types")


  def __init__(self, encryption_type: str):
    self.encryption_type = encryption_type

  def __repr__(self):
    return "Encryption Type [id: {0} , type: {1}]".format(self.encryptionType_id, self.encryption_type)


class CesarEncryptionTB(EncryptionType):

  __tablename__ = "cesar_encryption"

  cesar_id = Column(Integer, ForeignKey("encryption_type.encryptionType_id"), primary_key=True, autoincrement=True)
  shift = Column(Integer)


  def __init__(self, shift: int):

    self.shift = shift
    self.encryption_type = " cesar encryption "

  def __repr__(self):
    return "Cesar Encryption [id: {0} , offset: {1}]".format(self.cesar_id, self.shift)


class MonoalphapaticSubtitution(EncryptionType):

  __tablename__ = "monoalphapatic_subtitution"

  monoalpha_id = Column(Integer, ForeignKey("encryption_type.encryptionType_id"), primary_key=True, nullable=False)

  def __init__(self):

    self.encryption_type = "mono alphabetic substitution"

  def __repr__(self):
    return "MonoalphapaticSubtitution Encryption [Id: {0}]".format(self.monoalpha_id)



