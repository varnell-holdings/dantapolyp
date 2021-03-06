"""Find a name in a csv file."""

import csv
import os
import pickle

from fuzzyfinder import fuzzyfinder


def main():
    fn = os.path.join(os.path.dirname(__file__), 'patients.py')
    with open(fn, 'rb') as patpick:
        pat_list =pickle.load(patpick)
    while True:
        query_string = input('Name in lower case, q to quit:  ')
        if query_string == 'q':break
        suggestions = fuzzyfinder(query_string, pat_list)
        print(list(suggestions))

if __name__ == '__main__':
    main()
