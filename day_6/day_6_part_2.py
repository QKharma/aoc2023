from functools import reduce

file = []
with open('day_6_input.txt') as f:
    file = [' '.join(line.strip().split()) for line in f.readlines() if line.strip() != '']

race = [int(''.join(x.split(':')[1].strip().split(' '))) for x in file]

print(race)

result = []

race[1] = i*(race[0]-i)

possible_durations = []
for i in range(race[0]+1):
    if race[1] < i*(race[0]-i):
        possible_durations.append(i)

result.append(len(possible_durations))

print(reduce(lambda x, y: x * y, result))
