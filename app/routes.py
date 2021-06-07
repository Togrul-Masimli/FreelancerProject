from flask import render_template, url_for, redirect
from wtforms.validators import Email
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from flask_login import login_user


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/add-project')
def add_prj():
    return render_template('add-project.html', title='Add Project')

@app.route('/profile')
def profile():
    return render_template('profile.html', title='Profile')

@app.route('/profiles')
def profiles():
    return render_template('profiles.html', title='Profiles')

@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')

@app.route('/single-project')
def sing_project():
    return render_template('single-project.html', title='Single Project')

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html', title='Forgot Password')


@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))
    return render_template('sign-in.html', title='Sign In', form=form)


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('sign_in'))
    return render_template('sign-up.html', title='Sign Up', form=form)