# make email list
# extracts email addresses from a textfile and puts them in the clipboard for pasting

# the list of emails needs to be in a textfile called "emails" located on desktop
f = '/Users/ethan/Desktop/emails.txt'
f_ile = open(f)
f_txt = f_ile.read()

# use regex module to find email addresses
# this snippet lifted from: http://stackoverflow.com/questions/17681670/extract-email-sub-strings-from-large-document
import re
match = re.findall(r'[\w\.-]+@[\w\.-]+', f_txt)

# put the emails in a string that can be copied and pasted
output = ", ".join(match)

#output data to the clipboard
import subprocess

# can't remember where this came from - probably stackoverflow
def setClipboardData(data):
	p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
	p.stdin.write(data)
	p.stdin.close()
 	retcode = p.wait()

setClipboardData(output)