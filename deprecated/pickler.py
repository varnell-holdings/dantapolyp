import csv
import pickle

with open('dantastudy.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    pat_list = []
    for row in csvreader:
        patient = row[0].lower()
        pat_list.append(patient)
print(pat_list)
with open('patients2.py', 'wb') as patpick:
    pickle.dump(pat_list, patpick)
