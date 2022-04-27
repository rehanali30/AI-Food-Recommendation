from recommendation import menu
from emotion import get_emotion

from flask import Flask, request, make_response, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import LoginForm, SignupForm

from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config["SECRET_KEY"] = "password"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/food'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            login_user(user)
            flash("Login Succesfull!")
            return redirect('emotion')
        else:
            flash("That User Doesn't Exist! Please Try Again")
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
	logout_user()
	flash("You Have Been Logged Out!")
	return redirect('/')



@app.route("/signup", methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        form.name.data = ''
        form.email.data = ''
        flash("User Added Successfully!")

    return render_template('signup.html', form=form)



@app.route('/emotion', methods=['POST', 'GET'])
@login_required
def capture_img():
    if request.method == "POST":
        global emotion, msg, img
        emotion, msg, img = get_emotion(request.form["img"])
        return redirect('/recommend')
    
    return render_template('emotion.html')

@app.route('/recommend', methods=['GET'])
@login_required
def recommend():
    if emotion=='angry':
        food = 'Chocolate'
    elif emotion=='disgust':
        food = 'Watermelon Juice'
    elif emotion=='fear':
        food = 'Smoothies'
    elif emotion=='happy':
        food = 'Pizza'
    elif emotion=='neutral':
        food = 'Popcorn'
    elif emotion=='sad':
        food = 'Cake'
    elif emotion=='surprise':
        food = 'Pasta'
    return render_template('recommend.html', msg=msg, img=img, menu=menu, food=food)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)





