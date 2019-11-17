from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from scraping.abreviationScraper import getSchools
@app.route('/')
@app.route('/index')
def index():
    colors = ['Red', 'Blue', 'Black', 'Orange']
    user = {'username': 'Gireesh'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    schools = getSchools()

    return render_template('index.html', title='Home', user=user, posts=posts, colors=schools)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)