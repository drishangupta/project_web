#! /usr/bin/python3
print("Content-type:text/html")
print()

import boto3
import cgi, subprocess
import cgitb; cgitb.enable()

# Get filename here.
form=cgi.FieldStorage()
fileitem = form['file']
s3=boto3.client('s3',aws_access_key_id='AKIA6OE37FXCZQYCILZC',aws_secret_access_key="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")
# Test if the file was uploaded
import subprocess

if fileitem.filename:
    file_data = fileitem.file.read()
    file_name = fileitem.filename
    try:
        s3.upload_fileobj(fileitem.file, "filesupload2202",file_name)
        print("<h2>File Uploaded Successfully!</h2>")
    except Exception as e:
        print("<h2>error {} </h2>",format(e))


else:
   print("<h2> ERROR </h2>")
