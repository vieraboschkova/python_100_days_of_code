# with open("./025_csv/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("./025_csv/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = list()
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append((row[1]))
#         print(row)
#     print(temperatures)

import pandas

# data = pandas.read_csv("./025_csv/weather_data.csv")
# print(data)
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data.temp.to_list()
# print(temp_list)

# print(data[data.day == "Monday"])
# CONDITION GOES IN THE SWUARE brackets!
# print(data[data.temp == data.temp.max()])

# data = {
#         "students": ["A", "B", "C"],
#         "scores": [5,5,4],
# }

# data_from_dict = pandas.DataFrame(data)
# data_from_dict.to_csv("pandas.csv")
# print(data_from_dict)

# SQUIRRELS

data = pandas.read_csv("./025_csv/squirrels_data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)

data_dict = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./025_csv/squirrels_count.csv")