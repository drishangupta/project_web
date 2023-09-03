#!/usr/bin/python3
print("Content-type:text/html")
print()
import cgi
import pywhatkit as pwk
data=cgi.FieldStorage()
number = data.getvalue("number")    
message = data.getvalue("message")
    

if message and number:
       pwk.sendwhatmsg_instantly("918426881469"," message")
else:
        print("Please enter both the message and the number.")
