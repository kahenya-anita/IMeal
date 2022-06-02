from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin,LoginManager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    usertype = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))

    orders = db.relationship('Orders', backref='users',lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'

class Meals(db.Model):
    __tablename__="meals"

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    ingredients = db.Column(db.String(255))
    cost = db.Column(db.Integer)
    deleted = db.Column(db.Boolean)
    menu_id = db.Column(db.Integer, db.ForeignKey('menuday.id'), nullable=True)

    menuday = db.relationship('Menuday',foreign_keys=menu_id)
    orders = db.relationship('Orders',backref = 'meals',lazy="dynamic")
    #picture  = db.Column(db.String(255))

class Menuday(db.Model):
    __tablename__="menuday"

    id = db.Column(db.Integer,primary_key = True)
    mealdate = db.Column(db.String(255))
    
    ##function to return the meals for a given date

class Orders(db.Model):
    __tablename__="orders"

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    meal_id = db.Column(db.Integer,db.ForeignKey('meals.id'))

    ##add a total cost Column


    #userId foreignkey, mealid, mealcost
