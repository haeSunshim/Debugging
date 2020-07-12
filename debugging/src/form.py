from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, Email, Regexp, EqualTo, ValidationError
from debugging.src.data import Host, Refugee, User

# register for host
class RegisterForm(FlaskForm):
    name = StringField(
        validators=[
            DataRequired("name cannot be empty"),
        ],
        description="name",
        render_kw={
            "placeholder": "enter name please！",
        }
    )
    email = StringField(
        validators=[
            DataRequired("Email cannot be empty！"),
            Email("Enter correct Email please！")
        ],
        description="Email",
        render_kw={
            "type": "email",
            "placeholder": "enter email Please！",
        }
    )
    pwd = PasswordField(
        validators=[
            DataRequired("password cannot be empty！")
        ],
        description="password",
        render_kw={
            "placeholder": "Enter password Please！",
        }
    )
    repwd = PasswordField(
        validators=[
            DataRequired("Enter pasword agian！"),
            EqualTo('pwd', message="password are not same！")
        ],
        description="confirm your password",
        render_kw={
            "placeholder": "enter your password again！",
        }
    )
    submit = SubmitField(
        'register',
        render_kw={
            "class": "btn btn-primary",
        }
    )
    '''
    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError("The email already exists！")
    '''

# login form
class LoginForm(FlaskForm):
    email = StringField(
        validators=[
            DataRequired("Email cannot be empty！")
        ],
        description="Email",
        render_kw={
            "type"       : "email",
            "placeholder": "Please enter Email！",
        }
    )
    pwd = PasswordField(

        validators=[
            DataRequired("The password cannot be empty！")
        ],
        description="password",
        render_kw={
            "type"       : "password",
            "placeholder": "enter password please！",
        }
    )
    submit = SubmitField(
        'login',
        render_kw={
            "class": "btn btn-primary",
        }
    )

# refugee form
class RefugeeForm(FlaskForm):
    housename = StringField(
        validators=[
            DataRequired("house name cannot be empty"),
        ],
        description="house name",
        render_kw={
            "placeholder": "enter house name please！",
        }
    )
    contact = StringField(
        validators=[
            DataRequired("Phone number cannot be empty！"),
        ],
        description="Contact",
        render_kw={
            "placeholder": "enter Contact Please！",
        }
    )
    guest = StringField(
        validators=[
            DataRequired("guest number cannot be empty！")
        ],
        description="guest number",
        render_kw={
            "placeholder": "Enter guest number Please！",
        }
    )
    address = StringField(
        validators=[
            DataRequired("address cannot be empty！")
        ],
        description="address",
        render_kw={
            "placeholder": "Enter address Please！",
        }
    )
    suburbs = StringField(
        validators=[
            DataRequired("suburbs cannot be empty！")
        ],
        description="suburbs",
        render_kw={
            "placeholder": "Enter suburbs Please！",
        }
    )
    submit = SubmitField(
        'post',
        render_kw={
            "class": "btn btn-primary",
        }
    )