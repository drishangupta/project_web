#!/usr/bin/python3
print("Content-type:text/html")
print()

import subprocess
 
images = subprocess.getoutput("sudo docker images")
print("<h2>")
print("<pre>")
print(images)
print("</pre>")
print("</h2>")
