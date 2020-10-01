from flask import render_template, request, redirect,url_for,abort
from flask_login import LoginManager,login_user,login_required
from . import main
from .forms import UpdateProfile
from .. import db
from ..models import User,Meals,Menuday,Orders


@main.route('/')

def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/orders/<int:orders_id>')
@login_required
def orders(movie_id):

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
    uname = 'Abdi'
    title='Dashboard'
    total_orders = Orders.query.count()
    orders = Orders.query.all()
    total_sales = 0
    for order in orders:
        meal_cost = order.meals.cost
        total_sales +=meal_cost

    return render_template('admin/dashboard.html',uname=uname,title=title,total_orders = total_orders,total_sales=total_sales)

@main.route('/user/admin/menu/<uname>', methods=['GET','POST'])
@login_required
def admin_menu(uname):
    return render_template('admin/menu.html')

@main.route('/user/admin/orders/<uname>', methods=['GET','POST'])
@login_required
def admin_orders(uname):
    return render_template('admin/orders.html')