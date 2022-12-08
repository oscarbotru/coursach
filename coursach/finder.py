import csv
import os


def cache(func):

    def wrapper(*args, **kwargs):
        cache_name = ''.join(*args) + ''.join(kwargs.values())

        if os.path.exists(f'cache/{cache_name}.csv'):
            with open(f'cache/{cache_name}.csv') as cache_file:
                reader = csv.DictReader(cache_file)
                result = [*reader]
        else:
            result = func(*args, **kwargs)

            with open(f'cache/{cache_name}.csv', 'w') as cache_file:
                cache_file.writelines(result)

        return result
    return wrapper


@cache
def get_by_date(*args, **kwargs):

    with open('data/result.csv') as result_file:
        for row in result_file.readline():
            print(row)
