import data_scilib.functions as f

def small_tests():
    print("\nStarting tests with small dataset.")

    analyzer = f.analyzer('tests_files/small_dataset.csv')

    first_test = analyzer.rows_num()
    print(f"\nCalculating how many rows (without header) the file has. Found: {first_test} rows.")

    second_test = analyzer.columns_num()
    print(f"\nCalculating how many columns the file has. Found: {second_test} columns.")

    third_test = analyzer.find_value_in_row('Username', 'Sam')
    print(f"\nLooking for value of column 'Username' in the row where value 'Sam' is present in any column. Found: {third_test[0]} is the value for 'Username' in the row where value 'Sam' is present.")


    fourth_test = analyzer.is_empty('Last name')
    print(f"\nLooking for the row where the value for column 'Last name' is empty. Found: row #{fourth_test[0]} has no value in column 'Last name'.")

    fifth_test = analyzer.count_if([
        ('Active', lambda x: x == "No"), 
        ('Age', lambda x: x >= 30), 
        ('Location', lambda x: x < 10) # Last condition will return 0 matches since you're trying to compare a string with a number. IMPORTANT: an exception will not be thrown.
    ])
    print(f"\nCalculating how many rows have the value 'No' in the 'Active' column. Found: {fifth_test[0]} rows.") 
    print(f"\nCalculating how many rows have a value greater than or equal to 30 in the 'Age' column. Found: {fifth_test[1]} rows.")
    print(f"\nCalculating how many rows have a value less than 10 in the 'Location' column. Found: {fifth_test[2]} rows. IMPORTANT: returns 0 because all values in 'Location' are strings.")

    sixth_test = analyzer.max_min([
        'Age',
        'First name', # will return ['-inf', 'inf'] since column has no numerical values
    ])
    print(f"\nLooking for the maximum and minimum value for 'Age' across all rows. Found: {sixth_test[0][0]} is the maximum and {sixth_test[0][1]} the minimum.")
    print(f"\nLooking for the maximum and minimum value for 'First name' across all rows. Found: {sixth_test[1][0]} is the maximum and {sixth_test[1][1]} the minimum. IMPORTANT: -inf and inf are returned since all values in 'Last name' are strings.")

def large_tests():
    print("\nStarting tests with large dataset.")

    analyzer = f.analyzer('tests_files/large_dataset.csv')

    first_test = analyzer.rows_num()
    print(f"\nCalculating how many rows (without header) the file has. Found: {first_test} rows.")

    second_test = analyzer.columns_num()
    print(f"\nCalculating how many columns the file has. Found: {second_test} columns.")

    third_test = analyzer.find_value_in_row('total_deaths', 'Mexico')
    print(f"\nLooking for value of column 'total_deaths' in the row where value 'Mexico' is present in any column. Found: {len(third_test)} rows, {third_test[-1]} is the value in column 'total_deaths' for the last found row.")

    fourth_test = analyzer.count_if([
        ('total_cases', lambda x: x >= 500000), 
        ('icu_patients', lambda x: x >= 1000),
        ('continent', lambda x: x == "Asia")
    ])
    print(f"\nCalculating how many rows have a value greater than or equal to 500,000 in the 'total_cases' column. Found: {fourth_test[0]} rows.") 
    print(f"\nCalculating how many rows have a value greater than or equal to 1,000 in the 'icu_patients' column. Found: {fourth_test[1]} rows.")
    print(f"\nCalculating how many rows have a value equal to 'Asia' in the 'continent' column. Found: {fourth_test[2]} rows.")

    fifth_test = analyzer.max_min([
        'total_cases',
        'total_deaths'
    ])
    print(f"\nLooking for the maximum and minimum value for 'total_cases' across all rows. Found: {fifth_test[0][0]} is the maximum and {fifth_test[0][1]} the minimum.")
    print(f"\nLooking for the maximum and minimum value for 'total_deaths' across all rows. Found: {fifth_test[1][0]} is the maximum and {fifth_test[1][1]} the minimum.")

    sixth_test = analyzer.average('new_deaths')
    print(f"\nCalculating average value for 'new_deaths' across all rows. Found: {sixth_test}.")

if __name__ == '__main__':
    small_tests()
    large_tests()