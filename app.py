from flask import Flask, render_template, request, Session
import persistence

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def hello_world():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']

        persistence.create_user(firstname, lastname)

        return render_template('formInfo.html', un = firstname, ln=lastname)

    return render_template('home.html')


@app.route('/<string:firstname>/')
def display_name(firstname):
    userInfo = persistence.get_user(firstname)
    return userInfo.firstname + ' ' + userInfo.lastname

if __name__ == '__main__':
    app.run(port='80')
