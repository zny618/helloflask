from flask import Flask
from flask import url_for
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello():
    return '<h1>hello flask!<h1><img src="http://helloflask.com/totoro.gif">'
@app.route('/home')
def home():
    return 'This is a home show!'
@app.route('/user/<name>')
def user_page(name):
    return f'User:{escape(name)}'

@app.route('/test')
def test_url_for():
    # follow is some example(http://localhost:5000/test after cmd windows print URL)
    print(url_for('hello'))                 # print:/index
    print(url_for('user_page', name='zny'))   # print:/user/zny
    print(url_for('user_page', name='xiaoyu')) #print:/user/xiaoyu
    print(url_for('test_url_for')) # print:/test
    # follow this is def up more num , it can be query string add URL flow
    print(url_for('test_url_for', num=2)) # print:/rest?num2
    return 'Test page'
