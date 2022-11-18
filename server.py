from flask import Flask
from flask import request
from flask import redirect
import random

app = Flask(__name__)

nextId = 4
topics = [
    {'id':1, 'title':'html', 'body':'html is...'},
    {'id':2, 'title':'css', 'body':'css is...'},
    {'id':3, 'title':'js', 'body':'js is...'}
]



@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2><p>Hello, Web</p>') 
    
@app.route('/hello')
def hello():
    return 'Welcome'

@app.route('/read1/<id>')
def read1(id):
    print(id)
    return 'Read1' + id
# -------------------------------------READ-----------------------------------------

# def template(contents, content):
#     return f'''
#     <html>
#         <body>
#             <h1><a href='/'>WEB</a></h1>
#             <ol>
#                 {contents}
#             </ol>
#             {content}
#         </body>
#     </html>
#     '''

def getContents():
    liTags = ''

    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return liTags

# @app.route('/read/<int:id>')
# def read(id):  
#     title = ''
#     body = ''

#     for topic in topics:
#         if(id == topic['id']):
#             title = topic['title']
#             body = topic['body']
#             break

#     return template(getContents(), f'<h2>{title}</h2><p>{body}</p>')
# -----------------------------Create------------------------------
# def template(contents, content):
#     return f'''
#     <html>
#         <body>
#             <h1><a href='/'>WEB</a></h1>
#             <ol>
#                 {contents}
#             </ol>
#             {content}
#             <ul>
#                 <li><a href ="/create">Create</a></li>
#             </ul>
#         </body>
#     </html>
#     '''

@app.route('/create', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create" method="POST">
                <p><input type = "text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder = "body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id':nextId, 'title':title, 'body':body}
        topics.append(newTopic)
        url = '/read/' + str(nextId)
        nextId = nextId + 1
        return redirect(url)
# --------------------------Update----------------------------
# def template(contents, content, id = None):
#     contextUI = ''
#     if id != None:
#         contextUI = f'''
#             <li><a href = "/update/{id}">Update</a></li>
#         '''
#     return f'''
#     <html>
#         <body>
#             <h1><a href='/'>WEB</a></h1>
#             <ol>
#                 {contents}
#             </ol>
#             {content}
#             <ul>
#                 <li><a href ="/create">Create</a></li>
#                 {contextUI}
#             </ul>
#         </body>
#     </html>
#     '''

# @app.route('/read/<int:id>')
# def read(id):  
#     title = ''
#     body = ''

#     for topic in topics:
#         if(id == topic['id']):
#             title = topic['title']
#             body = topic['body']
#             break

#     return template(getContents(), f'<h2>{title}</h2><p>{body}</p>',id)

# @app.route('/update/<int:id>', methods = ['GET', 'POST'])
# def update(id):
#     if request.method == 'GET':
#         title = ''
#         body = ''

#         for topic in topics:
#             if id == topic['id']:
#                 title = topic['title']
#                 body = topic['body']
#                 break
#         content = f'''
#             <form action="/update/{id}" method="POST">
#                 <p><input type = "text" name="title" placeholder="title" value="{title}"></p>
#                 <p><textarea name="body" placeholder = "body">{body}</textarea></p>
#                 <p><input type="submit" value="update"></p>
#             </form>
#         '''
#         return template(getContents(), content)
#     elif request.method == 'POST':
#         title = request.form['title']
#         body = request.form['body']
#         for topic in topics:
#             if id == topic['id']:
#                 topic['title'] = title
#                 topic['body'] = body
#                 break
#         url = '/read/' + str(id)
#         return redirect(url)

def template(contents, content, id = None):
    contextUI = ''
    if id != None:
        contextUI = f'''
        <li><a href = "/update/{id}">update</a></li>
        '''
    return f'''
    <html>
        <body>
            <h1><a href='/'>WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href ="/create">Create</a></li>
                {contextUI}
            </ul>
        </body>
    </html>
    '''
@app.route('/read/<int:id>')
def read(id):  
    title = ''
    body = ''

    for topic in topics:
        if(id == topic['id']):
            title = topic['title']
            body = topic['body']
            break

    return template(getContents(), f'<h2>{title}</h2><p>{body}</p>', id)

@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        title = ''
        body = ''
        for topic in topics:
            if id == topic['id']:
                title = topic['title']
                body = topic['body']
                break

        content = f'''
            <form action="/update/{id}" method = "POST">
                <p><input type="text" name = "title" placeholder="title" value="{title}"></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="update"></p>
            </form>
        '''
        return template(getContents() ,content)

    elif request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        for topic in topics:
            if id == topic['id']:
                 topic['title'] = title
                 topic['body'] = body
                 break
        url = '/read/' + str(id)
        return redirect(url)

app.run(port=5001 ,debug = True)