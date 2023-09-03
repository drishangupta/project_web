#!/usr/bin/python3
print("Content-type:text/html")
print()

import cgi
import subprocess

data = cgi.FieldStorage()
image_name = data.getvalue("image")

result = subprocess.run(["docker", "rmi", image_name], capture_output=True, text=True)

if result.returncode == 0:
    print(f"Image '{image_name}' removed successfully.")
else:
    print(f"Error removing image: {result.stderr}")

