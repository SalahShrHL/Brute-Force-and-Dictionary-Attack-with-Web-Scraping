
from turtle import title
from flask import Flask, render_template , url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import InputRequired, Length, ValidationError , Regexp  
from flask_bcrypt import Bcrypt
from sqlalchemy import *


app = Flask(__name__) 
################################# BDD  #############################################################################


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)



################################# LOGIN MANEGER ####################################################################


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


################################ BDD ###############################################################################
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password1 = db.Column(db.String(80), nullable=False)
    password2 = db.Column(db.String(80), nullable=False)
    password3 = db.Column(db.String(80), nullable=False)
    #__table_args__ = (CheckConstraint("regexp_like(password1 ,(0|1)+ )",name='c1'),)
    # __table_args__ = (CheckConstraint(password1.regexp_match('(0-9)*'),name='c1'))
# CheckConstraint(func.REGEXP_LIKE(User.password1, '(0-9)*'), name='c1')

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_em = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    id_rp =db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    content= db.Column(db.String(400), nullable=False)

#################################  FORMES   #########################################################################

# REGISTER #

class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": ""})
    email= StringField(validators=[
                           InputRequired(), Length(min=4, max=80)], render_kw={"placeholder": ""})
    password1 = PasswordField(validators=[
                             InputRequired(), Length(min=3, max=3),Regexp("[0|1]{3}", message="password1 must contain only 0 and 1")], render_kw={"placeholder": ""})
    password2 = PasswordField(validators=[
                             InputRequired(), Length(min=5, max=5),Regexp("[0-9]{5}", message="password1 must contain only number from 0 to 9")], render_kw={"placeholder": ""})
    password3 = PasswordField(validators=[
                             InputRequired(), Length(min=5, max=5)], render_kw={"placeholder": ""})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')

# Login  #

class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": ""})

    password2 = PasswordField(validators=[
                             InputRequired(), Length(min=5, max=5)], render_kw={"placeholder": ""})

    submit = SubmitField('Login')


#################################  ROUTES     ########################################################################
@app.route("/",methods=['GET', 'POST'])
def Loginpage():
  form = LoginForm()

  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user:
          if (user.password2==form.password2.data):
              login_user(user)
              return redirect(url_for('Send_message'))

  return render_template("login.html" , title="Login page",form=form)



@app.route("/register",methods=['GET', 'POST'])
def Registerpage():
  form = RegisterForm()

  if form.validate_on_submit():
    #hashed_password = bcrypt.generate_password_hash(form.password2.data)
    new_user = User(username= form.username.data , email=form.email.data , password1=form.password1.data,password2=form.password2.data,password3=form.password3.data)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('Loginpage'))

  return render_template("register.html", title="Register page",form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('Loginpage'))


@app.route("/Mes_Contactes", methods=['GET', 'POST'])
@login_required
def Send_message():
  users = User.query.all()
  u_id = current_user.id
  return render_template("EnvoyerM.html", title="Send message", users=users,u_id =u_id)



@app.route("/ListesMss", methods=['GET', 'POST'])
@login_required
def Messegs_list():
  return render_template("ListesM.html", title="Messegs list")



@app.route("/WriteMss", methods=['GET', 'POST'])
@login_required
def Write_message():
  return render_template("Chat.html", title="Write message")

################################################################################################

if __name__ == "__main__":
  app.run(debug=True, port=9009)