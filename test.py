topics = [
    {'id':1, 'title':'html', 'body':'html is...'},
    {'id':2, 'title':'css', 'body':'css is...'},
    {'id':3, 'title':'js', 'body':'js is...'}
]

liTags = ''

for topic in topics:
    liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'

print(liTags)