#This is a new script, using CGI features

import cgi

#We also create a FieldStorage object for info

info=cgi.FieldStorage()

#Assign your selected option to the variable called sport

sport=info.getvalue('SportList')

print('Content-type:text/html\r\n')

print('<!DOCTYPE HTML>')

print('<html lang="en">')

print('<head><meta charset="UTF-8">')

print('<title>Python Response</title></head>')

print('<body>')

print('<h1>Sport:',sport,'</h1>')

print('<a href="selectionlist.html">Back to Main</a>')

print('</body>')

print('</html>')

#Save the two files in your Web server / htdocs directory.
