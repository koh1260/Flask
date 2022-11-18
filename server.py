from flask import Flask
import random

app = Flask(__name__)

topics = [
    {'id':1, 'title':'html', 'body':'html is...'},
    {'id':2, 'title':'css', 'body':'css is...'},
    {'id':3, 'title':'js', 'body':'js is...'}
]

def template(contents, content):
    return f'''
    <html>
        <body>
            <h1><a href='/'>WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
        </body>
    </html>
    '''

@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return template(liTags, '<h2>Welcome</h2><p>Hello, Web</p>') 
    
@app.route('/hello')
def hello():
    return 'Welcome'

@app.route('/create')
def create():
    return 'Create'

@app.route('/read1/<id>')
def read1(id):
    print(id)
    return 'Read1' + id
# -------------------------------------READ-----------------------------------------
@app.route('/read/<int:id>')
def read(id):  
    liTags = ''
    title = ''
    body = ''

    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    for topic in topics:
        if(id == topic['id']):
            title = topic['title']
            body = topic['body']
            break

    return template(liTags, f'<h2>{title}</h2><p>{body}</p>')

app.run(port=5001 ,debug = True)