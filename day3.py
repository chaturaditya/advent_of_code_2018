lines = [line.rstrip('\n') for line in open('./input_day3.txt')]

new_lines = []
for line in lines:
    line = re.split(' @ |,|: |x|#',line)
    line.pop(0)
    new_lines.append(line)