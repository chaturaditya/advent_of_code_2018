import csv

results = []
with open('input_day1.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(int(row[0]))
## PART ONE
print(sum(results))


## PART TWO
seen = [0]
done = False
iters = 0
while done == False:
    for i,result in enumerate(results):
        calc = result + seen[i+iters]
        if calc in seen:
            done = True
            print(calc)
            break
        else:
            seen.append(result + seen[i+iters])
    iters+=len(results)