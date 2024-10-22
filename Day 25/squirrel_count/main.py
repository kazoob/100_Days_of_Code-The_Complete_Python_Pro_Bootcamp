import pandas

squirrel_file = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(squirrel_file[squirrel_file["Primary Fur Color"] == "Gray"])
black_squirrels = len(squirrel_file[squirrel_file["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(squirrel_file[squirrel_file["Primary Fur Color"] == "Cinnamon"])

print(gray_squirrels)
print(black_squirrels)
print(cinnamon_squirrels)

squirrels = {
    "color": ["gray", "black", "cinnamon"],
    "count": [gray_squirrels, black_squirrels, cinnamon_squirrels],
}

print(squirrels)

pandas.DataFrame(squirrels).to_csv("output.csv")
