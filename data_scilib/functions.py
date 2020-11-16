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
This function prints the whole csv file except for the first row (header)
"""
def print_no_header(file):
  with open(file, newline='') as csvfile:
    spamreader=csv.reader(csvfile,delimiter=',', quotechar='|')
    next(spamreader) # Skips first row
    for row in spamreader:
      print(', '.join(row))

"""
This function returns the number of rows in the csv file
"""
def rows_num(file):
  with open(file, newline='') as csvfile:
    spamreader=csv.reader(csvfile,delimiter=',', quotechar='|')
    return(len(list(spamreader)) - 1) # subtract 1 to not count header
    
    # TODO: check for empty rows
    

"""
This function returns the number of columns in the csv file
"""
def columns_num(file):
  with open(file, newline='') as csvfile:
    spamreader=csv.reader(csvfile,delimiter=',', quotechar='|')
    return(len((list(spamreader))[0]))

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
    raise Exception(f"Column '{column}' not found")
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
  # suggestions: 1. a function that accounts for when there are 2 of the same thing 2. 

"""
Checks how many rows (excluding the header) satisfy the condition given by a lambda function in the column specified.
The input type is of array to enable multiple conditions in multiple columns. The array should be of tuples in the form: (column, condition), where column is a string and condition a lambda function
"""
def count_if(file, conditions):
  column_indeces = [-1] * len(conditions)
  result = [0] * len(conditions)

  with open(file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
    header = next(spamreader)
    for index, condition in enumerate(conditions):
      if condition[0] in header:
        column_indeces[index] = header.index(condition[0])
      else:
        raise Exception(f"Column '{condition[0]}' not found.")

    for row in spamreader:
      for index, condition in enumerate(conditions):
        try:
          if condition[1](row[column_indeces[index]]):
            result[index] += 1
        except Exception:
            try:
              if condition[1](int(row[column_indeces[index]])):
                result[index] += 1
            except Exception:
              pass
  
  return result