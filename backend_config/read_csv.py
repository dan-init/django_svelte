import csv

with open('CDT Data.csv', 'r') as file:
    reader = csv.reader(file)

    return_list = []

    for row in reader:
        if row not in return_list:
            return_list.append(row)
        else:
            pass

print(return_list)

    