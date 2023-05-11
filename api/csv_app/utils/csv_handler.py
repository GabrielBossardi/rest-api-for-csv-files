import csv


def generate_dict(file, header):
    csv_data = []
    full_file_name = file + '.csv'
    with open(full_file_name, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            row_dict = dict(zip(header, row))
            row_dict = {
                key: (None if value == '' else value)
                for key, value in row_dict.items()
            }
            csv_data.append(row_dict)

    return csv_data
