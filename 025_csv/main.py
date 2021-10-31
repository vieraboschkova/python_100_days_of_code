# with open("./025_csv/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

with open("./025_csv/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = list()
    for row in data:
        if row[1] != 'temp':
            temperatures.append((row[1]))
        print(row)
    print(temperatures)