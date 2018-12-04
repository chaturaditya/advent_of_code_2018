import csv

results = []
with open('input_day2.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(list(row[0]))

#PART 1
from collections import Counter
twos = 0
threes = 0
for i in results:
    set_ = set(Counter(i).values())
    if len(set_)==2 and 2 in set_:
        twos += 1
    elif len(set_)==2 and 3 in set_:
        print('hey')
        threes += 1
    elif len(set_)==3:
        twos+=1
        threes += 1
        
#print checksum
print(twos*threes)


#PART 2
for i in results:
    for j in results:
        if i!=j:
            x = [a == b for a, b in zip(i, j)]
            if x.count(False)==1:
                print(i,j)