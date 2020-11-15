import csv

"""
This function prints the whole csv file
"""
def print_all(file):
  with open(file, newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
      print(', '.join(row))

"""
This function prints the whole csv file except for the first row
"""
def print_no_first(file):
  with open(file, newline='') as csvfile:
    spamreader=csv.reader(csvfile,delimiter=',', quotechar='|')
    next(spamreader) # Skips first row
    for row in spamreader:
      print(', '.join(row))


"""
This function will return a list containing the rows where the specified element appears
"""
def find_element(file, element):
  rows = []

  with open(file, newline='')as csvfile:
    spamreader=csv.reader(csvfile,delimiter=',', quotechar='|')
    next(spamreader) # Skips first row
    for row in spamreader:
      if element in row: # Check each row to check if element is present
        rows.append(row)          
          
  return rows

"""
This function will find the value of the column specified by "column" in the row where the "element" is present. The "column" parameter needs to be in the first row of the csv file.
"""
def find_value_in_row(file, column, element):
  column_index = -1
  found = []

  with open(file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
    header = next(spamreader)
    for i in range(len(header)):
      if header[i] == column:
        column_index = i
        break

  # If the "column" was not found on the first row of the file, raise an exception
  if column_index == -1:
    raise Exception("The column specified was not found")
    return []

  rows = find_element(file, element) # Use already defined function to find the rows where "element" appears

  for row in rows:
    found.append(row[column_index])

  return found

"""
This function will check if any row is empty on the "column" specified. If it is empty, it will and the row index (0 based, index 0 is header row) to the array returned.
"""
def is_empty(file, column):
  column_index = -1
  empty = []

  with open(file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
    header = next(spamreader)
    for i in range(len(header)):
      if header[i] == column:
        column_index = i
        break
    
    counter = 0
    for row in spamreader:
      counter += 1
      if row[column_index].strip() == '':
        empty.append(counter)

  return empty