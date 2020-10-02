# iteratively rename files

import os
import glob 

# change extension as needed
extension = '.csv'

for n, file in enumerate(glob.glob('*' + extension)):
    with open(file,'r') as f:
        newfile = 'participant' + str(n+1) + extension
        os.rename(file, newfile)
