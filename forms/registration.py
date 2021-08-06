from .__form_modules import *


class RegistrationForm(FlaskForm):
    email = StringField("Login/Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password_repeated = PasswordField("Repeat password", validators=[DataRequired()])
    submit = SubmitField("Submit")

