from .__form_modules import *


class LoginForm(FlaskForm):
    email = StringField("Login/Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

