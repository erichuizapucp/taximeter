import csv
import os

train_file_name = 'train_data.csv'
val_file_name = 'val_data.csv'
test_file_name = 'test_data.csv'


def get_number_samples(data_file_path):
    no_rows = 0
    with open(data_file_path) as data_file:
        data_file_reader = csv.DictReader(data_file)
        next(data_file_reader, None)
        for entry in data_file_reader:
            no_rows = no_rows + 1
    return no_rows


def split_source_file(data_file_path, no_rows, split_dist=(0.6, 0.1, 0.3)):
    train_percentage = split_dist(0)
    val_percentage = split_dist(1)
    test_percentage = split_dist(2)

    data_set_folder_path = os.path.basename(data_file_path)
    train_file_path = os.path.join(data_set_folder_path, train_file_name)
    val_file_path = os.path.join(data_set_folder_path, val_file_name)
    test_file_path = os.path.join(data_set_folder_path, test_file_name)

    no_train_rows = int(no_rows * train_percentage)
    no_val_rows = int(no_rows * val_percentage)
    no_test_rows = int(no_rows * test_percentage)

    return train_file_path, val_file_path, test_file_path
