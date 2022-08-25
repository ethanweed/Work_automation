# Collects all text from .md files in a folder into one .md file

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
