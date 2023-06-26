<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def economic_calendar_page():
	return render_template('economic_calendar.html', calendar=economic_calendar)

if __name__ == '__main__':
	app.run()
=======
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html', name = current_user.name)
>>>>>>> bc
