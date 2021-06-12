import os
import secrets
from PIL import Image
from flask import render_template, url_for, redirect, request, abort
from wtforms.validators import Email
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdateInfoForm, UpdateProfileForm, PostForm, CommentForm
from app.models import User, Post, UserInfo, Comment
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def index():
    posts = Post.query.all()
    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile-pictures/' + current_user.image_file )
        return render_template('index.html', image_file=image_file, posts=posts)
    return render_template('index.html', posts=posts)

@app.route('/add-project', methods=['GET','POST'])
@login_required
def add_prj():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, min_pay=form.cost_min.data, max_pay=form.cost_max.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add-project.html', title='Add Project', form=form, legend='New Project')

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    image_file = url_for('static', filename='profile-pictures/' + current_user.image_file )
    return render_template('profile.html', title='Profile', image_file=image_file, form=form)

@app.route('/profile/info')
def info():
    image_file = url_for('static', filename='profile-pictures/' + current_user.image_file )
    return render_template('profile_info.html', title='User Info', image_file=image_file)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile-pictures', picture_fn)

    output_size = (120, 120)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route('/profile/settings', methods=['GET','POST'])
def settings():
    form = UpdateProfileForm()
    formInfo = UpdateInfoForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('settings'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    # if formInfo.validate_on_submit():
    #     owner = current_user
    #     owner.speciality = formInfo.speciality.data
    #     current_user.info.location = formInfo.location.data
    #     current_user.info.age = formInfo.age.data
    #     current_user.info.experience = formInfo.experience.data
    #     db.session.commit()
    #     return redirect(url_for('settings'))
    if formInfo.validate_on_submit():
        userinfo = UserInfo(speciality=formInfo.speciality.data, location=formInfo.location.data, age=formInfo.age.data, experience=formInfo.experience.data, owner=current_user)
        db.session.add(userinfo)
        db.session.commit()
        return redirect(url_for('settings'))
    # elif request.method == 'GET':
    #     owner = current_user
    #     formInfo.speciality.data = current_user.speciality
    #     formInfo.location.data = current_user.info.location
    #     formInfo.age.data = current_user.info.age
    #     formInfo.experience.data = current_user.info.experience
    image_file = url_for('static', filename='profile-pictures/' + current_user.image_file )
    return render_template('profile_settings.html', title='Settings', image_file=image_file, form=form, formInfo=formInfo)

@app.route('/profiles')
def profiles():
    return render_template('profiles.html', title='Profiles')

@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html', title='Forgot Password')

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
    return render_template('sign-in.html', title='Sign In', form=form)

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('sign_in'))
    return render_template('sign-up.html', title='Sign Up', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/projects/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('single-project.html', title=post.title , post=post)


@app.route('/projects/<int:post_id>/update', methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.min_pay = form.cost_min.data
        post.max_pay = form.cost_max.data
        db.session.commit()
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.cost_min.data = post.min_pay
        form.cost_max.data = post.max_pay
    return render_template('add-project.html', title='Update Post' , post=post, legend='Update Post', form=form)


@app.route('/projects/<int:post_id>/delete', methods=['GET','POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))