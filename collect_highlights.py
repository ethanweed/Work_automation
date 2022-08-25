# Collects all text from .md files in a folder into one .md file

# I use the app Highlights (https://highlightsapp.net) to mark up pdf files. Highlights generates .md "sidecar" files containing highlighted text and notes.
# I use this script to gather all the notes from these sidecar files into one .md file called "highlights.md"
# This file can be viewed in e.g. Marked2 (https://marked2app.com) or Obsidian (http://obsidian.md/) and (thanks to Highlights) contains hyperlinks back to the original pdfs.

import os
path = 'PATH/TO/MARKDOWN/FILES'
files = [file for file in os.listdir(pathin) if file.endswith('.md')]
for file in files:
    f = open(file)
    text = f.read()
    highlights = open(path + 'highlights.md', 'a')
    highlights.write(text)
    highlights.write('----- \n') 
    highlights.write('\n') 
    highlights.close()
