import math 
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n= len(data)
    total =0
    for x in data:
        total +=int(x)

    mean = total/ n
    return mean

squared_lists = []
for number in data:
    a = int(number) - mean(data)
    a= a**2
    squared_lists.append(a)

sum=0
for i in squared_lists:
    sum = sum +i

results = sum/ (len(data)-1)

str_deviation = math.sqrt(results)
print(str_deviation)