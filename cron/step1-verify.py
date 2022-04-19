"""
# Bad
# * * * * * wall "Hello world!"
0 * * * * wall "Hello world!"
* * * * * echo "Hello world!"
# Good
* * * * * wall Hello world!
* * * * * wall "Hello world!"
* * * * * wall "Custom text is also fine"
* * * * * wall Custom text is also fine
 * * * * * wall "Spacey boi"
"""


import re

with open("/var/spool/cron/crontabs/root") as f:
    contents = f.read()

if not re.search(r"^\s*\*\s*\*\s*\*\s*\*\s*\*\s*wall .+", contents, re.MULTILINE):
    with open("/root/output.txt") as f:
        f.write("Fail")
    raise Exception("Couldn't find a matching crontab command for the current user!")
with open("/root/output.txt") as f:
    f.write("Success")