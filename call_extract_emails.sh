#!/bin/bash
# I use this shell script embedded in a Hazel routine that watches the desktop for a file named "emails.txt"
# When such a file shows up, Hazel fires off this script, which then runs "extract_emails.py" on the "emails.txt"

cd /Users/ethan/Documents/Scripts/Work_automation/
python extract_emails.py

