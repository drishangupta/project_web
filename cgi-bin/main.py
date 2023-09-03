#!/usr/bin/python3
import subprocess
import cgi
print("content-type: text/html")
print()

data=cgi.FieldStorage()
cmd=data.getvalue("c")

data1=subprocess.getoutput("sudo "+cmd)
print("<pre>")
print(data1)
print("</pre>")
#print("<pre>")
#print(output[1])
#print("</pre>")
