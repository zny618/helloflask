from flask import Flask, render_template
from flask import url_for
from markupsafe import escape



app = Flask(__name__)

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]


@app.route('/')
@app.route('/index')
def index():
     return render_template('index.html', name=name, movies=movies)
    # return '<h1>hello flask!<h1><img src="http://helloflask.com/totoro.gif">'
@app.route('/home')
def home():
    return 'This is a home show!'
@app.route('/user/<name>')
def user_page(name):
    return f'User:{escape(name)}'

@app.route('/test')
def test_url_for():
    # follow is some example(http://localhost:5000/test after cmd windows print URL)
    print(url_for('index'))                 # print:/index
    print(url_for('user_page', name='zny'))   # print:/user/zny
    print(url_for('user_page', name='xiaoyu')) #print:/user/xiaoyu
    print(url_for('test_url_for')) # print:/test
    # follow this is def up more num , it can be query string add URL flow
    print(url_for('test_url_for', num=2)) # print:/rest?num2
    return 'Test page'
