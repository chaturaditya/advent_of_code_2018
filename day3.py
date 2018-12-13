import re
import pandas as pd
from collections import Counter
lines = [line.rstrip('\n') for line in open('./input_day3.txt')]

new_lines = []
for line in lines:
    line = re.split(' @ |,|: |x|#',line)
    line.pop(0)
    new_lines.append(line)
    
df = pd.DataFrame(new_lines, columns = ['A','left','top','width','height'])
df = df.set_index(df.A)
df = df.drop(['A'],axis=1)
df = df.astype(int)
df['x'] = df.left+df.width
df['y'] = df.top+df.height
df.left = df.left+1
df.top = df.top+1

ranges1 = []
ranges2 = []
for index, row in df.iterrows():
    ranges1.append(set(range(row['left'],row['x']+1)))
    ranges2.append(set(range(row['top'],row['y']+1)))
    
counter = 0
seen_range1 = set()
seen_range2 = set()
for i in range(len(ranges1)):
    for j in range(len(ranges2)):
        
        if(i!=j):
            intersect1 = set.intersection(ranges1[i], ranges1[j])
            intersect2 = set.intersection(ranges2[i], ranges2[j])

            A = intersect1.difference(seen_range1)
            B = intersect2.difference(seen_range2)

            seen_range1.update(A)
            seen_range2.update(B)

            counter = counter+(len(A)*len(B))
print(counter)
    
count_list = []
for index, row in df.iterrows():  
    for i in range(row['width']):
        for j in range(row['height']):
            count_list.append((i+row['width'],j+row['height']))

print(len(Counter(count_list)))