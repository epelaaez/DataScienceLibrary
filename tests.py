import data_scilib.functions as f

def tests():
    print(f.find_value_in_row('tests_files/small_dataset.csv', 'Username', 'Sam'))
    print(f.is_empty('tests_files/small_dataset.csv', 'Last name'))
    print(f.rows_num('tests_files/small_dataset.csv'))
    print(f.columns_num('tests_files/small_dataset.csv'))

if __name__ == '__main__':
    tests()