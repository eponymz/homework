import cgi

info=cgi.FieldStorage()

company=info.getavalue('Company')

Phone=info.getvalue('phone')

print('content-type:text/html\n')

print('<!DOCTYPE HTML>')

print('<html lang="en">')

print('<head>')

print('<meta charset="UTF-8">')

print('<title>Response For Python</title>')

print('</head>')

print('<body>')

print('<h1>', company, phone, '</h1>')

print('<a href="postingofaform.html">Return to main</a>')

print('</body>')

print('</html>')
