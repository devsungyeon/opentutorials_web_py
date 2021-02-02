#!C:\Python39\python.exe
print("content-type: text/html; charset=utf-8\n")
import cgi
form = cgi.FieldStorage()
pageId = form["id"].value

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
        <li><a href="index.py?id=HTML">HTML</a></li>
        <li><a href="index.py?id=CSS">CSS</a></li>
        <li><a href="index.py?id=JavaScript">Javascript</a></li>
    </ol>

    <h2>{title}</h2>
    <P>
        Web is a computer programming system created by Donald E. Knuth as the first implementation of what he called "literate programming": the idea that one could create software as works of literature, by embedding source code inside descriptive text, rather than the reverse (as is common practice in most programming languages), in an order that is convenient for exposition to human readers, rather than in the order demanded by the compiler.

        Web consists of two secondary programs: TANGLE, which produces compilable Pascal code from the source texts, and WEAVE, which produces nicely-formatted, printable documentation using TeX.
    </P>
</body>
</html>
'''.format(title = pageId))