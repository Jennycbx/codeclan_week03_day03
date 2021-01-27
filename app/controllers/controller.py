from flask import render_template
from app import app
from app.models.shop_app import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Home', orders=orders)