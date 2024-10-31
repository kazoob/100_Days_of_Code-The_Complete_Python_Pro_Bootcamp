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

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# print(data["temp"])

# Challenge 4

import pandas
from numpy.ma.extras import average

data = pandas.read_csv("weather_data.csv")
print(data.to_dict())
print()

temp_list = data.temp.to_list()
print(temp_list)
print()

print(f"Average temperature (numpy): {int(average(temp_list))}")
print(f"Average temperature (panda): {int(data.temp.mean())}")
print()

print(f"Maximum temperature (panda): {data.temp.max()}")
print(f"Minimum temperature (panda): {data.temp.min()}")
print()

print(data[data.day == "Monday"])
print(data[data.day == "Monday"].condition)
print()

print(data[data.temp == data.temp.max()])
print(data[data.temp == data.temp.max()].temp)
print()

temp = data[data.day == "Monday"].temp[0]
print(f"{(temp * 9/5) + 32} F")
print()

