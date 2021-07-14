from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('homepage.html')


@app.route('/', methods=['POST'])
def render():
    names = ('uthmaan', 'malik', 'abdul', 'zaid', 'cassiem', 'aaliyah')
    text = request.form['full_name']
    # return processed_text

    for i in names:
        if text == i:
            return redirect(url_for('admin_user', name=text))
        else:
            return redirect(url_for('guest', name=text))


@app.route('/admin/<name>')
def admin_user(name):
    return 'Hello Admin %s' % name


@app.route('/guest/<name>')
def guest(name):
    return 'Hello guest %s' % name


if __name__ == '__main__':
    app.debug = True
    app.run()

