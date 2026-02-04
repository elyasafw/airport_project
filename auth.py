import csv


def user_loading(filename):
    matrix = []
    with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                matrix.append(row)
            return matrix

