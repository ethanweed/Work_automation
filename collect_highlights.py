# Collects all text from .md files in a folder into one .md file

# I use the app Highlights (https://highlightsapp.net) to mark up pdf files. Highlights generates .md "sidecar" files containing highlighted text and notes.
# I use this script to gather all the notes from these sidecar files into one .md file called "highlights.md"
# This file can be viewed in e.g. Marked2 (https://marked2app.com) or Obsidian (http://obsidian.md/) and (thanks to Highlights) contains hyperlinks back to the original pdfs.

import os
path = '/path/to/my/pdfs/'
files = [file for file in os.listdir(path) if file.endswith('.md')]
if '_highlights.md' in files:
	os.remove ('_highlights.md') 
files = [file for file in os.listdir(path) if file.endswith('.md')]
for file in files:
    f = open(file)
    text = f.read()
    highlights = open(path + '_highlights.md', 'a')
    highlights.write(text)
    highlights.write('----- \n') 
    highlights.write('\n') 
    highlights.close()
