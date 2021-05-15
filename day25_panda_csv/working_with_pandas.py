# import csv
#
# with open("weather_data.csv", 'r') as in_file:
#
#     data = csv.reader(in_file)
#     tempuratures = []
#     for row in data:
#         if row[1].isnumeric():
#             tempuratures.append(int(row[1]))
#
#     print(tempuratures)

import pandas

# data = pandas.read_csv('weather_data.csv')
#
# data_dict = data.to_dict()
#
# temp_list = data['temp'].to_list()
# avg_temps = sum(temp_list) / len(temp_list)
# print(temp_list, avg_temps)
#
# print(data.temp.max())
#
# print(data[data.temp == data.temp.max()])

"""
2018 Central Park Squirrel Census - Squirrel Data
"""
import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squirrel = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel = len(data[data['Primary Fur Color'] == 'Black'])

print(gray_squirrel)
print(red_squirrel)
print(black_squirrel)
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, red_squirrel, black_squirrel]
}
df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')