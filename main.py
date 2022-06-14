from flask import Flask
from flask import render_template, redirect, url_for

app = Flask(__name__)


# root of our website
@app.route('/')
def first_page():
    return redirect('homePage.html')


@app.route('/homePage.html')
def home_page():
    return render_template('homePage.html')


@app.route('/logIn.html')
def login():
    return render_template('logIn.html')


@app.route('/New_Audio_creator.html')
def new_audio():
    return render_template('New_Audio_creator.html')


@app.route('/Profile.html')
def profile():
    return render_template('Profile.html')


@app.route('/published.html')
def published():
    return render_template('published.html')


@app.route('/Register.html')
def register():
    return render_template('Register.html')


@app.route('/shared.html')
def shared():
    return render_template('shared.html')


@app.route('/templates.html')
def templat():
    return render_template('templates.html')


if __name__ == '__main__':
    app.run(debug=True)
