def sort_single_file(file_path):
    pass


def file_sorters(batches_count):
    print('-- start to sorting all files one by one')
    for i in range(batches_count):
        print(f'-- start to sort file number: {i}')
        sort_single_file(f'data/temp/{i + 1}.csv')
