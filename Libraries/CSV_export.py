import csv
from robot.api.deco import keyword

"""CSV Library"""
__all__ = ['clear_file', 'append_file']


@keyword('Clear file')
def clear_file(filepath):  # Clear_file :it will clear your file.
    with open(filepath, 'w+') as f:
        obj1 = csv.writer(f)


@keyword('Append file')
def append_file(filepath, data):  # Append_file :it will append the data you wanted to in your script.
    with open(filepath, 'a') as file:
        # csv.Dialect.delimiter = delimiter
        obj1 = csv.writer(file, delimiter='|', quoting=csv.QUOTE_NONE, escapechar=' ')
        obj1.writerow(data)