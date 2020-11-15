import data_scilib.functions as f

def tests():
    print(f.find_value_in_row('tests.csv', 'Username', 'Sam'))
    print(f.is_empty('tests.csv', 'Last name'))

if __name__ == '__main__':
    tests()