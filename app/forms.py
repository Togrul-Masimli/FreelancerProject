from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms import validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User, Tag

tags = Tag.query.all()

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is taken.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('UPDATE')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is taken.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email is taken.')

    # def validate_speciality(self, speciality):
    #     if speciality.data != current_user.speciality:
    #         user = User.query.filter_by(username=speciality.data).first()
    #         if user:
    #             raise ValidationError('This username is taken.')

class UpdateInfoForm(FlaskForm):
    speciality = StringField('Speciality', validators=[DataRequired()])
    location = StringField('Location')
    age = StringField('Age')
    experience = StringField('Experience')
    submit = SubmitField('UPDATE')


class PostForm(FlaskForm):
    title = StringField('Project name', validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    cost_min = StringField('Min', validators=[DataRequired()], render_kw={"placeholder": "Min"})
    cost_max = StringField('Max', render_kw={"placeholder": "Max"})
    submit = SubmitField('POST A PROJECT')


class CommentForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired()], render_kw={"placeholder": "Type your comment..."})
    submit = SubmitField('Submit')


class BidForm(FlaskForm):
    min_rate = StringField('Min', validators=[DataRequired()])
    max_rate = StringField('Max', validators=[DataRequired()])
    delivery_duration = StringField('Set Your Delivery Time', validators=[DataRequired()])
    submit = SubmitField('PLACE A BID')

