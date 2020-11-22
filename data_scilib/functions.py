import csv

def print_all(file):
  """
  This function prints the whole csv file
  """
  try:
    with open(file, newline = '') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
      for row in spamreader:
        print(', '.join(row))
  except FileNotFoundError:
    print(f'File "{file}" not found in function print_all')

def print_no_header(file):
  """
  This function prints the whole csv file except for the first row (header)
  """
  try:
    with open(file, newline='') as csvfile:
      spamreader=csv.reader(csvfile,delimiter=',', quotechar='|')
      next(spamreader) # Skips first row
      for row in spamreader:
        print(', '.join(row))
  except FileNotFoundError:
    print(f'File "{file}" not found in function print_no_header')

def rows_num(file):
  """
  This function returns the number of rows in the csv file
  """
  with open(file, newline='') as csvfile:
    spamreader=csv.reader(csvfile,delimiter=',', quotechar='|')
    return(len(list(spamreader)) - 1) # subtract 1 to not count header
    
    # TODO: check for empty rows
    
def columns_num(file):
  """
  This function returns the number of columns in the csv file
  """
  with open(file, newline='') as csvfile:
    spamreader=csv.reader(csvfile,delimiter=',', quotechar='|')
    return(len((list(spamreader))[0]))

def find_element(file, element):
  """
  This function will return a list containing the rows where the specified element appears
  """
  rows = []

  with open(file, newline='')as csvfile:
    spamreader=csv.reader(csvfile,delimiter=',', quotechar='|')
    next(spamreader) # Skips first row
    for row in spamreader:
      if element in row: # Check each row to check if element is present
        rows.append(row)          
          
  return rows

def find_value_in_row(file, column, element):
  """
  This function will find the value of the column specified by "column" in the row where the "element" is present. The "column" parameter needs to be in the first row of the csv file.
  """
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

  rows = find_element(file, element) # Use already defined function to find the rows where "element" appears

  for row in rows:
    found.append(row[column_index])

  return found

def is_empty(file, column):
  """
  This function will check if any row is empty on the "column" specified. If it is empty, it will add the row index (0 based, index 0 is header row) to the array returned.
  """
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


def count_if(file, conditions):
  """
  Checks how many rows (excluding the header) satisfy the condition given by a lambda function in the column specified.
  The input type is of array to enable multiple conditions in multiple columns. The array should be of tuples in the form: (column, condition), where column is a string and condition a lambda function
  """
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
              if condition[1](float(row[column_indeces[index]])):
                result[index] += 1
            except Exception:
              pass
  
  return result

def max_min(file, columns):
  """
  This function will return the maximum value and minimum value of each column specified in the "column" paramater. This parameter should be an array of strings with all the columns desired.
  The return value is an array of arrays, each inside array with contain the maximum and minimum value of the column in the same index in the "columns" paramter.
  IMPORTANT: the columns specified must have numerical values in at least 2 rows. It will return ['-inf', 'inf'] for columns that have no numerical values.
  """
  column_indeces = [-1] * len(columns)
  result = []
  for _ in range(len(columns)):
    result.append([float('-inf'), float('inf')])

  with open(file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
    header = next(spamreader)

    for index, column in enumerate(columns):
      if column in header:
        column_indeces[index] = header.index(column)
      else:
        raise Exception(f"Column '{column}' not found.")

    for row in spamreader:
      for n_column, index in enumerate(column_indeces):
        try:
          if float(row[index]) > result[n_column][0]:
            result[n_column][0] = float(row[index])
          if float(row[index]) < result[n_column][1]:
            result[n_column][1] = float(row[index])
        except Exception:
          pass

  return result
