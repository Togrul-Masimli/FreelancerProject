from flask import render_template, url_for, redirect
from app import app
from app.forms import RegistrationForm, LoginForm


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

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == '123':
            return redirect(url_for('index'))
    return render_template('sign-in.html', title='Sign In', form=form)


@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html', title='Forgot Password')


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('sign-up.html', title='Sign-up', form=form)