import data_scilib.functions as f

def tests():
    print(f.find_value_in_row('tests_files/small_dataset.csv', 'Username', 'Sam'))
    print(f.is_empty('tests_files/small_dataset.csv', 'Last name'))
    print(f.rows_num('tests_files/small_dataset.csv'))
    print(f.columns_num('tests_files/small_dataset.csv'))
    print(f.count_if('tests_files/small_dataset.csv', [
        ('Active', lambda x: x == "No"), 
        ('Age', lambda x: x >= 30), 
        ('Location', lambda x: x < 10) # Last condition will return 0 matches since you're trying to compare a string with a number. IMPORTANT: an exception will not be thrown.
    ])) 
    print(f.max_min('tests_files/small_dataset.csv', [
        'Age',
        'First name', # will return ['-inf', 'inf'] since column has no numerical value
    ]))    

if __name__ == '__main__':
    tests()