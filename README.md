# Data Science Library
As the name states it, this python library is aimed for use in data science programs where analyzing CSV files is needed. Functions similar to the most common ones in Excel are provided. 

## Installation
In order to install this library in your local machine, clone this repository by running:
```
git clone https://github.com/epelaaez/DataScienceLibrary.git
``` 
Be sure to have pip installed and run the following while being in the directory you cloned the repo in:
```
pip install .
```
To update the library, first run the following command to get the latest updates from the repo: 
```
git pull
```
After you get the latest updates pulled into your local machine, you need to run the installation command again and the library will be updated.

## Documentation
This library is class-oriented. You need to create an object in which you will run your desired function later. To create the object, run the following code:
```python
a = analyzer(path)
```
Where path is the path to the file you want to run the functions on. After you create the object, you can use dot notation to invoke any function you want. There are two types of functions: printing and returning. Printing functions will print something to the console and returning functions will return a value. All functions implemented at the moment are described below.

#### Printing functions:
```python
a.print_all()
```
This function will print the whole csv file given.

```python
a.print_no_header()
```
This function prints the whole csv file except for the first row; which is in most cases the header where columns are specified.

#### Returning functions:
```python
a.rows_num()
```
This function returns the number of rows in the csv file, not counting the first one since it is the header.  
Return value:
- Integer corresponding to the number of rows in the csv file, excluding the header.

```python
a.columns_num()
```
This function returns the number of columns in the csv file. Only uses the first row to do the counting.   
Return value:
- Integer corresponding to the number of columns in the csv file.

```python
a.find_element(element)
```
This function will return an array containing the rows where the specified element appears. It skips the first row, so the header will never be included in the returned array.   
Parameters:
- element: value you are looking for in your file.   

Return value:
- An array of arrays, where each inside array is each row where the element specified was found.

```python
a.find_value_in_row(column, element)
```
This function will return an array with the value of the column specified in the rows where the element given is present. Depends on last function to find the rows where the given element is present.   
Parameters:
- column: column from which you want to retrieve the value.
- element: element that needs to be present in the rows from where you want to retrieve the value in the column specified.   

Return value:
- An array with the values found, it will be of the size of the number of the rows where the element specified is present. The values will be in the same order as those rows.

```python
a.is_empty(column)
```
This function will check if any row is empty on the column specified. Empty means that there is no value for the given column. If it is empty, it will add the row index to the array returned.   
Parameters:
- column: column that you want to check for emptiness in each row.   

Return value:
- An array with the indeces of the rows where the column specified is emtpy. Indeces are 0 based, where 0 corresponds to the header.

```python
a.count_if(conditions)
```
Checks how many rows (excluding the header) satisfy the condition given by a lambda function in the column specified. More than one condition and column can be given; all conditions will be independent from one another.   
Parameters:
- conditions: an array of tuples of the form (column, condition), where column is a string specifying the column to look at and condition a lambda function against which the value in the column will be tested.   

Return value:
- An array of integers (in the same order of the conditions parameter) which correspond to the number of rows that satisfied given condition.

```python
a.max_min(columns)
```
This function will return the maximum and minimum value of each column specified in the column paramater among all the rows of the file. IMPORTANT: the columns specified must have numerical values in at least one row to ensure that the return value is not `['-inf', 'inf']`.   
Parameters:
- columns: an array of strings with all the columns to check for.   

Return value:
- An array of arrays, where each inside array (in the same order of the columns parameter) contains the maximum value found in index 0 and the minimum value found in index 1.

```python
a.average(column)
```
This function will return the average value of the given column. Each row that has no numeric value for the column will have no effect on the average or the number of rows considered. Thus, if there are no numeric values in the column specified, the average returned will be 0.   
Parameters:
- column: string with name of column you want the average of.   

Return value:
- Integer corresponding to the average for the given column.
