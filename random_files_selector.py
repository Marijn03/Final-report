# Marijn Jongsma
# 29-03-2022
# select_random_files.py
# This programs takes an input file that include filenames, select 10 unique filenames and 
# returns a text file with contains 10 random selected filenames

import os, random
import sys

def select_files(gz_files):
    """ select 10 unique random files from a text file and return this as
    a list
    """
    with open(gz_files, "r") as inp:
        set_of_files = set()
        allText = inp.read()
        while len(set_of_files) < 10:
            set_of_files.add(random.choice(list(map(str, allText.split()))))
        return list(set_of_files)

def main(argv):
    with open('random_selected_files.txt', 'w') as out:
        out.write(str(select_files(argv[1])))
    
if __name__ == '__main__':
    main(sys.argv)
