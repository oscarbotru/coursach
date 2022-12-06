import os
from shutil import rmtree

from coursach.configs import BATCH_SIZE
from coursach.file_divider import file_divider
from coursach.files_concatenator import concatenate_files
from coursach.files_sorter import file_sorters


def clear_files(batches_count):
    rmtree('data/temp')
    for i in range(batches_count - 1):
        os.remove(f'data/result{i + 1}.csv')

    os.rename(f'data/result{batches_count}.csv', 'data/result.csv')


def global_sorter():
    batches_count = file_divider('all_stocks_5yr.csv', BATCH_SIZE)
    file_sorters(batches_count)
    concatenate_files(batches_count)
    # clear_files(batches_count)
