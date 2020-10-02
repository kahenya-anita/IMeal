from flask import render_template, request, redirect,url_for,abort
from flask_login import LoginManager,login_user,login_required,current_user
from . import main
from .forms import UpdateProfile,AddMealForm
from .. import db
from ..models import User,Meals,Menuday,Orders


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')


@main.route('/about')
def about():

    '''
    View root page function that returns the about page and its data
    '''
    return render_template('about.html')

@main.route('/orders/<int:orders_id>')
@login_required
def orders(orders_id):

    '''
    View orders page function that returns the order details page and its data
    '''
    return render_template('orders.html',id = orders_id)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/admin/dashboard/<uname>', methods=['GET','POST'])
def admin_dashboard(uname):
    menu = Menuday(mealdate='Thursday')
    db.session.add(menu)
    db.session.commit()
    uname = current_user.username
    title='Dashboard'
    total_orders = Orders.query.count()
    orders = Orders.query.all()
    total_sales = 0
  
    return render_template('admin/dashboard.html',uname=uname,title=title,total_orders = total_orders,total_sales=total_sales)

@main.route('/user/admin/orders/<uname>', methods=['GET','POST'])
@login_required
def admin_orders(uname):
    uname= current_user.username
    orders = Orders.query.all()
    return render_template('admin/orders.html',orders=orders)

@main.route('/user/admin/meals/<uname>', methods=['GET','POST'])
@login_required
def admin_meals(uname):
    uname =current_user.username
    title="Meals"
    meals = Meals.query.all()
    return render_template('admin/meals.html',title = title,meals=meals)

@main.route('/user/admin/meals/delete/<meal_id>', methods=['GET','POST'])
@login_required
def delete_meal(meal_id):
    uname = current_user.username
    Meals.query.filter_by(id=meal_id).delete()
    db.session.commit()
    return redirect(url_for('.admin_meals',uname=current_user.username))

@main.route('/user/admin/meals/add/<uname>', methods=['GET','POST'])
@login_required
def add_meal(uname):
    form = AddMealForm()
    if form.validate_on_submit():
        meal_name = form.name.data
        meal_ingredients=form.ingredients.data
        meal_cost = form.cost.data
        new_meal = Meals(name=meal_name,ingredients=meal_ingredients,cost=meal_cost)
        db.session.add(new_meal)
        db.session.commit()
        
        return redirect(url_for('.admin_meals',uname=current_user.username))
    return render_template('admin/add-meal.html',form=form)

@main.route('/user/admin/menu/<uname>', methods=['GET','POST'])
@login_required
def admin_menu(uname):
    uname=current_user.username
    title='Menu'
    menu=Menuday.query.filter_by(mealdate='Thursday').first()
    meals = Meals.query.filter_by(menu_id = menu.id).all()

    return render_template('admin/menu.html',meals = meals,title=title)

@main.route('/user/admin/menu/set/<uname>', methods=['GET','POST'])
@login_required
def set_menu(uname):
    uname=current_user.username
    meals = Meals.query.all()
    title="Set"
    return render_template('admin/set-menu.html',title=title,meals=meals)

@main.route('/user/admin/menu/add/<meal_id>', methods=['GET','POST'])
@login_required
def add_menu(meal_id):
    menu = Menuday.query.filter_by(mealdate='Thursday').first()
    meal = Meals.query.filter_by(id=meal_id).first()
    meal.menu_id=menu.id
    db.session.add(meal)
    db.session.commit()
    return redirect(url_for('.set_menu',uname=current_user.username))

