# Makes use of the scholar.py Google Scholar parser available here:
# https://github.com/ckreibich/scholar.py
# to run a list of citations collected from other sources (PubMed, PsychINFO, etc.) through
# Google Scholar to return a consistent format and saved as a .csv file.
# This can be imported into a spreadsheet for quicker sorting when conducting a literature review

# For input, the script requires a .txt document with citations to be entered in Google Scholar,

import os
import re
import subprocess
import random as r

# these may not be needed, but I have on occasion run into search limit problems with Google Scholar
# timing searches with a jittered delay may help - I'm not sure
#import time
#d = r.random()*100
#delay = 18000+d

os.chdir('/Users/ethan/Desktop/')
file = 'titles.txt'

with open(file,'r') as f:
    text = f.read()
    text = re.split("(?m)^\s*$\s*", text)
    text = [s.replace('\n', '') for s in text]
    

os.chdir('/Users/ethan/Documents/Scripts/scholar.py')

citations = []
tot = len(text)

search_item = '-A ' + '"' + text[0] + '"' + ' --csv'
print search_item


for s, val in enumerate(text):    
    search_item = '-A ' + '"' + val + '"' + ' --csv'
    count = str(s+1)
    print count + ' of ' + str(tot)

    proc = subprocess.Popen(['python', 'scholar.py',  search_item], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    citation = proc.communicate()[0]

    citation = citation.split('\n')
    citation = [s.strip() for s in citation]


    citation_delim = []
    for s, val in enumerate(citation):
        print val
        item = val + '|'
        citation_delim.append(item)


    citations.append(citation_delim)
    
    
    #time.sleep(delay)
    
print citations

import re

# make a new text file with the output
header = 'title|url|year|num_citations|num_versions|cluster_id|url_pdf|url_citations|url_versions|url_citation|excerpt \n'
with open('/Users/ethan/Desktop/scholar_output.csv', 'a+') as newfile:
    newfile.write(header)
newfile.close()

temp = citations
tot = len(temp)


for s,val in enumerate(temp):
    newline = ''.join(val)
    newline = newline[0:-2]
    newline = re.sub('Title ', '', newline)
    newline = re.sub('URL ', '', newline)
    newline = re.sub('Year ', '', newline)
    newline = re.sub('Citations ', '', newline)
    newline = re.sub('Versions ', '', newline)
    newline = re.sub('Versions list ', '', newline)
    newline = re.sub('Excerpt Objectives ', '', newline)
    newline = re.sub('Cluster ID ', '', newline)
    newline = re.sub('Excerpt ', '', newline)
    newline = re.sub('list ', '', newline)
    newline = str(newline) + '\n'
    print newline
    with open('/Users/ethan/Desktop/scholar_output.csv', 'a+') as newfile:
        newfile.write(newline)
    newfile.close()
    count = str(s+1)
    print count + ' of ' + str(tot)
print 'All done!'