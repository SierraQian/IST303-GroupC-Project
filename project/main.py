from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def economic_calendar_page():
	return render_template('economic_calendar.html', calendar=economic_calendar)

if __name__ == '__main__':
	app.run()
