file = []
with open('day_1_input.txt') as f:
    file = f.read()
file = file.split('\n')

sum = 0

for s in file:
    values = []
    for c in s:
        if c.isnumeric():
            values.append(c)
    sum += int('{}{}'.format(values[0],values[-1]))

print(sum)
