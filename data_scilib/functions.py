import csv

def test(file):
    with open(file, newline = '') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
      for row in spamreader:
        print(', '.join(row))