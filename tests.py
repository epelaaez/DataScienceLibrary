import data_scilib.functions as f

def tests():
    print("Starting tests with small dataset.")

    first_test = f.rows_num('tests_files/small_dataset.csv')
    print(f"\nCalculating how many rows (without header) the file has. Found: {first_test} rows.")

    second_test = f.columns_num('tests_files/small_dataset.csv')
    print(f"\nCalculating how many columns the file has. Found: {second_test} columns.")

    third_test = f.find_value_in_row('tests_files/small_dataset.csv', 'Username', 'Sam')
    print(f"\nLooking for value of column 'Username' in the row where value 'Sam' is present in any column. Found: {third_test[0]} is the value for 'Username' in the row where value 'Sam' is present.")


    fourth_test = f.is_empty('tests_files/small_dataset.csv', 'Last name')
    print(f"\nLooking for the row where the value for column 'Last name' is empty. Found: row #{fourth_test[0]} has no value in column 'Last name'.")

    fifth_test = f.count_if('tests_files/small_dataset.csv', [
        ('Active', lambda x: x == "No"), 
        ('Age', lambda x: x >= 30), 
        ('Location', lambda x: x < 10) # Last condition will return 0 matches since you're trying to compare a string with a number. IMPORTANT: an exception will not be thrown.
    ])
    print(f"\nCalculating how many rows have the value 'No' in the 'Active' column. Found: {fifth_test[0]} rows.") 
    print(f"\nCalculating how many rows have a value greater than or equal to 30 in the 'Age' column. Found: {fifth_test[1]} rows.")
    print(f"\nCalculating how many rows have a value less than 10 in the 'Location' column. Found: {fifth_test[2]} rows. IMPORTANT: returns 0 because all values in 'Location' are strings.")

    sixth_test = f.max_min('tests_files/small_dataset.csv', [
        'Age',
        'First name', # will return ['-inf', 'inf'] since column has no numerical values
    ])
    print(f"\nLooking for the maximum and minimum value for 'Age' across all rows. Found: {sixth_test[0][0]} is the maximum and {sixth_test[0][1]} the minimum.")
    print(f"\nLooking for the maximum and minimum value for 'First name' across all rows. Found: {sixth_test[1][0]} is the maximum and {sixth_test[1][1]} the minimum. IMPORTANT: -inf and inf are returned since all values in 'Last name' are strings.")

if __name__ == '__main__':
    tests()