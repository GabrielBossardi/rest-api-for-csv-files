import csv


def generate_dict(file, header):
    csv_data = []
    full_file_name = file + '.csv'
    with open(full_file_name, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            csv_data.append(dict(zip(header, row)))

    return csv_data
