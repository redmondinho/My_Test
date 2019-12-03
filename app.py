from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/page2')
def page2():
	return 'Page 2'


if __name__ == '__main__':
    app.run()