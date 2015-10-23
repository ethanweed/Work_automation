# Submit_kortlink
# Ethan Weed
# 2015-20-10 

# take link from clipboard, submit to the link-shortening service kortlink.dk
# and return the shortened link to the clipboard

# dependencies:
# selenium: http://www.seleniumhq.org
# java SE development kit (required by selenium): http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html


from selenium import webdriver
import subprocess

# Sources:
# Clipboard handling snippets are copied from
# http://www.macdrifter.com/2011/12/python-and-the-mac-clipboard.html
#
# Selenium browser control based on
# https://automatetheboringstuff.com/chapter11/#calibre_link-12

# functions to read and write from clipboard
def getClipboardData():
 p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
 retcode = p.wait()
 data = p.stdout.read()
 return data

def setClipboardData(data):
 p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
 p.stdin.write(data)
 p.stdin.close()
 retcode = p.wait()

# get the link to be shortened from the clipboard
long_link = getClipboardData()

# define browser to be controlled by selenium
browser = webdriver.Firefox()

type(browser)

# point browser at kortlink.dk
browser.get('http://kortlink.dk')

# get the handle of the text box 
form_field = browser.find_element_by_name('url')

# enter the link to be shortened in the text box
form_field.send_keys(long_link)

# submit the form
form_field.submit()

# get the handle of the returned shortened link
link_elem = browser.find_element_by_partial_link_text('kortlink')

# send the short link to the clipboard
link_text = link_elem.text
data = link_text
print(data)
setClipboardData(data)


