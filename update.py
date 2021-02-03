#!C:\Python39\python.exe
print("content-type: text/html; charset=utf-8\n")
print()
import cgi, os
form = cgi.FieldStorage()

files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href=index.py?id={name}>{name}</a></li>'.format(name = item)

if 'id' in form:
    pageId = form["id"].value
    description = open('data/' + pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'

print('''
<!DOCTYPE html>
<html>
<head>
    <title>WEB1 - WEB</title> 
    <meta charset="utf-8">
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
        {listStr}
    </ol>
    <a href="create.py">create</a>
    <form action="process_update.py" method="POST">
        <input type="hidden" name="pageId" value="{form_default_title}">
        <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
        <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
        <p><input type="submit"></p>
    </form>
    <h2>{title}</h2>
    <P>{desc}</P>
</body>
</html>
'''.format(title = pageId, desc=description, listStr=listStr, form_default_title=pageId, form_default_description=description))