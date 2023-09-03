#!/usr/bin/python3
print("Content-type:text/html")
print()

import cgi
import subprocess

data = cgi.FieldStorage()
image_name = data.getvalue("image")

result = subprocess.run(["sudo","docker", "pull", image_name], capture_output=True, text=True)

if result.returncode == 0:
    print(f"Image '{image_name}' pulled successfully.")
else:
    print(f"Error pulling image: {result.stderr}")

