from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/orders/<int:orders_id>')
def orders(movie_id):

    '''
    View orders page function that returns the order details page and its data
    '''
    return render_template('orders.html',id = orders_id)