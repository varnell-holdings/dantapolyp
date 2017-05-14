"""Find a name in a csv file."""

import csv

from fuzzyfinder import fuzzyfinder


def  get_names():
    with open('danta_study.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        pat_list = []
        for row in csvreader:
            patient = row[0].lower()
            pat_list.append(patient)
    return pat_list

def main():
    pat_list =get_names()
    while True:
        query_string = input('Name in lower case, q to quit:  ')
        if query_string == 'q':break
        suggestions = fuzzyfinder(query_string, pat_list)
        print(list(suggestions))

if __name__ == '__main__':
    main()
