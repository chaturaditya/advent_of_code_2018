import csv

results = []
with open('input_day1.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(int(row[0]))
print(sum(results))