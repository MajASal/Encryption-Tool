from Encryption.database.databaseTables import SqlAlchemyBase, User, EncryptedString, EncryptionType, CesarEncryptionTB, MonoalphapaticSubtitution
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def connet_to_database():
  engine = create_database()
  global session
  session = create_session(engine)


def create_database():

  engine = create_engine("sqlite:///C:/Users/ASUS/Documents/Python/flaskApp/data.db") # this path should be changed to the relevant path of the application on your pc
                                                                                      # otherwise you will get an error.
                                                                                      # Note: data.db should be in flaskApp so that the flask application can use the same database as the console.
  SqlAlchemyBase.metadata.create_all(engine)
  return engine


def create_session(engine):

  t_Session = sessionmaker(engine)
  cr_session = t_Session()

  return cr_session


def check_existing_users(user_name):
  user = User(user_name)
  #user.name = user_name
  existing_user = session.query(session.query(User).filter_by(name=user_name).exists()).scalar()
  if existing_user is False:
    session.add(user)
    session.commit()
  else:
    user = session.query(User).filter_by(name=user_name).first()
  return user


def add_username(name):

  username = User(name)
  session.add(username)
  session.commit()


def add_mono():
  monoalpha = MonoalphapaticSubtitution()
  session.add(monoalpha)
  session.commit()


def add_cesar(shift):
  cesar = CesarEncryptionTB(shift)
  session.add(cesar)
  session.commit()


def add_encrypted_string(encrypted_msg, username):

  user = session.query(User).filter(User.name == username).first()
  encryption = session.query(EncryptionType).order_by(EncryptionType.encryptionType_id.desc()).first()

  encrypted_string = EncryptedString(encrypted_msg, user.someid, encryption.encryptionType_id)
  session.add(encrypted_string)
  session.commit()
