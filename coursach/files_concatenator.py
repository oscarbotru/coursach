import csv
import datetime


def write_all_to_file(iterator_pointer, result_file):
    for row in iterator_pointer:
        result_file.writerow(row)


def concatenate_files(batches_count, sort_key):
    print('#' * 50)
    for i in range(batches_count):

        file_i = open(f'data/temp/{i + 1}.csv')

        reader_i = csv.DictReader(file_i)

        result_file = open(f'data/result{i + 1}.csv', 'w')
        result_writer = csv.DictWriter(result_file, [*reader_i.fieldnames])
        result_writer.writeheader()

        if i == 0:
            print('-- write first file to result files')
            write_all_to_file(reader_i, result_writer)
        else:
            print(f'-- write {i + 1} file to prev result')
            file_prev = open(f'data/result{i}.csv')
            prev_reader = csv.DictReader(file_prev)

            row_i = reader_i.__next__()
            prev_file_row = prev_reader.__next__()

            while True:
                try:
                    var_1 = float(row_i[sort_key])
                    var_2 = float(prev_file_row[sort_key])
                except:
                    var_1 = row_i[sort_key]
                    var_2 = prev_file_row[sort_key]

                if var_1 > var_2:
                    result_writer.writerow(prev_file_row)
                    try:
                        prev_file_row = prev_reader.__next__()
                    except:
                        write_all_to_file(reader_i, result_writer)
                        break

                else:
                    result_writer.writerow(row_i)
                    try:
                        row_i = reader_i.__next__()
                    except:
                        write_all_to_file(prev_reader, result_writer)
                        break

            file_prev.close()

        result_file.close()
        file_i.close()
