from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class CreateUserForm(FlaskForm):
    name = StringField("Nickname", validators=[DataRequired()])
    email = StringField("Email", validators=[Email()])
    password = PasswordField("Password", validators=[Length(4, 256)])
    submit = SubmitField("Sign me in")


# TODO: Create a LoginForm to login existing users
class ConfirmUserForm(FlaskForm):
    email = StringField("Email", validators=[Email()])
    password = PasswordField("Password", validators=[Length(4, 256)])
    submit = SubmitField("Log me in")


# TODO: Create a CommentForm so users can leave comments below posts
class CreateCommentForm(FlaskForm):
    body = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit comment")