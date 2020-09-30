from flask import render_template, redirect, url_for, flash,request
from . import auth
from ..models import User
from .forms import RegistrationForm
from .. import db
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import Usermixin


@auth.route('/logout')

def logout():
    logout_user()
    return redirect(url_for("main.index"))

    

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message('Welcome to Imeals','email/welcome_user',user.email,user=user)
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)
