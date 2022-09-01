# Collects all text from .md files in a folder into one .md file

# I use the app Highlights (https://highlightsapp.net) to mark up pdf files. Highlights generates .md "sidecar" files containing highlighted text and notes.
# I use this script to gather all the notes from these sidecar files into one .md file called "highlights.md"
# This file can be viewed in e.g. Marked2 (https://marked2app.com) or Obsidian (http://obsidian.md/) and (thanks to Highlights) contains hyperlinks back to the original pdfs.

import os
path = '/path/to/my/pdfs/'

# get a list of all the markdown files in the folder
files = [file for file in os.listdir(path) if file.endswith('.md')]

# if the script has been run before, delete the old collection of highlights and notes, so that I don't just append to it.
if '_highlights.md' in files:
	os.remove ('_highlights.md') 

# now that the old collection has been removed, rebuild the list of markdown files
files = [file for file in os.listdir(path) if file.endswith('.md')]

# grab the contents of each file, and throw it into the new "_highlights.md" file
for file in files:
    f = open(file)
    text = f.read()
    highlights = open(path + '_highlights.md', 'a')
    highlights.write(text)
    highlights.write('----- \n') 
    highlights.write('\n') 
    highlights.close()
