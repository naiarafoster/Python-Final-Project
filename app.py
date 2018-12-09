from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
import sqlite3
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['SECRET_KEY']='734df2116319b7212b4cff613ae848dc'


@app.route('/')
@app.route('/home')
def home():
    conn = sqlite3.connect('example2.db')

    c = conn.cursor()
    c.execute('Select * from products')
    products = c.fetchall()
    return render_template('home.html', products=products)


@app.route('/inventory')
def about():
    conn = sqlite3.connect('example2.db')

    c = conn.cursor()
    c.execute('Select * from inventory')
    inventory = c.fetchall()
    return render_template('inventory.html', inventory=inventory, title='List')
    return "<h2>About Page<h2>"

@app.route('/checkout')
def checkout():                                                         
    return render_template('checkout.html', title='Checkout')

@app.route('/register')
def register():
    form=RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)
