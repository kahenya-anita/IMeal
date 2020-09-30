from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin,LoginManager
from flask_admin import Admin,AdminIndexView
from flask_admin.contrib.sqla import ModelView

class Orders(db.Model):
    __tablename__="orders"

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    meal_id = db.Column(db.Integer,db.ForeignKey('meals.id'))
    
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure  = db.Column(db.String(255))
    

    orders = db.relationship('Orders', backref='user',lazy="dynamic")


    @property
    def password(self):

        def __repr__(self):
            return f'User {self.name}'
    

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255),index = True)
    user = db.relationship('User',backref = 'role',lazy="dynamic")
    email = db.Column(db.String(255),unique = True,index = True)    
    password_hash = db.Column(db.String(255))
    name = db.Column(db.String)
    prof_pic_path = db.Column(db.String)
    bio = db.Column(db.String)
    password_secure = db.Column(db.String(255))

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('home.html'))

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

admin = Admin(index_view=MyAdminIndexView())
admin.add_view(ModelView(User, db.session))


@property
def password(self):
    raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)



    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    

    def __repr__(self):
        return f'User {self.name}'




class Meals(db.Model):
    __tablename__="meals"

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    ingredients = db.Column(db.String(255))
    cost = db.Column(db.Integer)
    deleted = db.Column(db.Boolean)

    menuday = db.relationship('Menuday',backref = 'meals',lazy="dynamic")
    orders = db.relationship('Orders',backref = 'meals',lazy="dynamic")
    #picture  = db.Column(db.String(255))

class Menuday(db.Model):
    __tablename__="menuday"

    id = db.Column(db.Integer,primary_key = True)
    mealdate = db.Column(db.String(255))
    meal_id = db.Column(db.Integer,db.ForeignKey('meals.id'))



    #userId foreignkey, mealid, mealcost
