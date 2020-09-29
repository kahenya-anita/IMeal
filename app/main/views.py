from flask import render_template, request, redirect,url_for
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/orders/<int:orders_id>')
def orders(movie_id):

    '''
    View orders page function that returns the order details page and its data
    '''
    return render_template('orders.html',id = orders_id)