from flask import Flask, render_template,flash ,flash, url_for , redirect, session, request
from functools import wraps
from flaskApp import db, app, bcrypt, User
from flaskApp.forms import LoginForm, RegistraionForm, EncryptionForm
from Encryption.Monoalpha import monoEncryption
from Encryption.CesarEncryption import encoding
from Encryption.database.databaseTables import EncryptionType
from Encryption.database.databaseMethods import add_cesar, add_mono, add_encrypted_string, connet_to_database
import random
import requests

#creates the database if it dosent exist
db.create_all()

def encryption_input_required(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    if 'encryption_method' in session:
      return func(*args, **kwargs)
    else:
      flash("no encrpytion input was given, please do that first", "danger")
      return redirect("/encryption")
  return wrapper

def login_required(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    if 'username' in session:
      return func(*args, **kwargs)
    else:
      flash('Please login first.','danger')
      return redirect('/login')
  return wrapper

#shows the current registered users
@app.route('/users', methods=['GET'])
@login_required
def users():
  results = db.session.query(User).all()
  return render_template('users.html', user = results)

@app.route('/',methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if 'username' in session:
    flash("You are already logged in.", "danger")
    return render_template('login.html', form=form)

  if form.validate_on_submit():
    user = db.session.query(User).filter_by(name=form.username.data).first()
    #if user and bcrypt.check_password_hash(user.user_password, form.password.data): #in case we used hashed password
    if user and user.user_password == form.password.data: ## this is new , in the last commit i forgot to add == form.password.data
      session['username'] = user.name
      return redirect(url_for('encryption'))
    else:
      flash('Login unsuccessful. please check your username and password', 'danger')
  return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistraionForm()
    if form.validate_on_submit():
        #hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # in case we want to hash the passwords (for security reasons)
        user = User(name=form.username.data,user_password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
@login_required
def logout():
  session.clear()
  session.pop('username', None)
  session.pop('encryption_type', None)
  session.pop('encryption_input', None)
  flash("You have successfully logged out, now you can log in again.", "success")
  return redirect(url_for('login'))


@app.route('/encryption', methods=['GET', 'POST'])
@login_required
def encryption():
  form = EncryptionForm()
  if form.validate_on_submit():
    connet_to_database()
    type1 = request.form['encryption_type']
    u_input = request.form['encryption_input']
   

    if type1 == 'cesar':
      try:
        offset = request.form['offset']

        if offset.isdigit():
            offset = request.form['offset']
        else:
            offset=random.randint(0,1024) 

        result = str(encoding(offset, u_input))
      except ValueError:
        offset=random.randint(0,1024)
        result=str(encoding(offset, u_input))
      session['offset'] = str(offset)

      add_cesar(offset)
    else:
      result = str(monoEncryption(u_input))
      add_mono()

    session['encryption_method'] = type1
    session['encrypted_string'] = result
    session['user_input'] = u_input

    username = str(session['username'])
    add_encrypted_string(result,username)
    return redirect('/result')

  return render_template('encryption.html', title='Encryption', form=form)


@app.route('/result', methods=['GET'])
@login_required
@encryption_input_required
def result():
    method_r = session['encryption_method']
    result_r = session['encrypted_string']
    input_r = session['user_input']
    if method_r == 'cesar':
        offset_r = session['offset']
        return render_template('result.html', title='Result', encryptiontype=method_r, offset=offset_r, unencoded_string=input_r, encrypted_string=result_r)#----------------------neu---------------------------------------#
    return render_template('result.html', title='Result', encryptiontype=method_r, offset='none', unencoded_string=input_r, encrypted_string=result_r)#----------------------neu---------------------------------------#

@app.route('/chuckjokes', methods=['GET'])
@login_required
def chuckjokes():
  response = requests.get("http://api.icndb.com/jokes/random")
  response_body = response.json() #parse response into json dictionary
  return render_template('chuckjokes.html', title='Chuck Jokes',joke=response_body)

@app.route("/catfact",methods=['GET'])
@login_required
def catfacts():  
    response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1")
    response_body = response.json()
    return render_template('catfacts.html', title='Cat Facts', catfact=response_body)

if __name__ == '__main__':
  app.run(debug=True)
