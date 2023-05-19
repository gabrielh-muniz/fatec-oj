from flask import (
  render_template,
  request, 
  flash,
  redirect,
  url_for,
)

from flask_login import (
  login_user,
  login_required,
  logout_user,
  current_user,
)

from ..models.User import User
from ..data.database import database as db
from ..extensions import bcrypt
from flask_bcrypt import generate_password_hash, check_password_hash

def login():
  if request.method == 'POST':
    email, password = request.form.values()

    user = User.query.filter_by(email=email).first()
    if user:
      if check_password_hash(user.password, password):
        flash(f'Logado com sucesso! Bem vindo {user.username}', category='success')
        login_user(user, remember=True)
        return redirect(url_for('view.home'))
      else:
        flash('Credenciais incorretas. Tente novamente!', category='error')
    else:
      flash('Email não cadastrado!', category='error')
  return render_template('login.html', user=current_user)

def sign_up():
  if request.method == 'POST':
    email, name, password1, password2 = request.form.values()

    user = User.query.filter_by(email=email).first()
    if user:
      flash('Email já está cadastrado!', category='error')
    elif len(email) < 4:
      flash('Email deve ter pelo menos 4 caracteres', category='error')
    elif len(name) < 2:
      flash('O nome deve conter pelo menos 2 caracteres', category='error')
    elif password1 != password2:
      flash('As senhas devem ser iguais', category='error')
    elif len(password1) < 7:
      flash('A senha deve conter pelo menos 7 caracteres', category='error')
    else:
      new_user = User(
        email = email,
        username = name,
        password = bcrypt.generate_password_hash(password1) 
      )
      db.session.add(new_user)
      db.session.commit()
      flash('Conta criada com sucesso', category='success')
      login_user(new_user, remember = True)
      return redirect(url_for('view.home'))
  return render_template('signup.html', user=current_user)

@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login')) 

@login_required
def home():
  return render_template('home.html', user=current_user)
