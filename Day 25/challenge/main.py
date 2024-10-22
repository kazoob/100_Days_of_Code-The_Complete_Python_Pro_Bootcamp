# Challenge 1

# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
# print(data)


# Challenge 2

# import csv
#
# with open("weather_data.csv") as weather_file:
#     # Skip first line
#     next(weather_file)
#     data = csv.reader(weather_file)
#     temperatures = []
#
#     for row in data:
#         print(row)
#         temperatures.append(int(row[1]))
#
#     print(temperatures)

# Challenge 3

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
