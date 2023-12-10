from datetime import datetime
startTime = datetime.now()

from functools import reduce
import math

file = []
with open('day_6_input.txt') as f:
    file = [' '.join(line.strip().split()) for line in f.readlines() if line.strip() != '']

race = [int(''.join(x.split(':')[1].strip().split(' '))) for x in file]

result = []

possible_durations = []

for i in range(race[0], 0, -1):
    if race[1] < i*(race[0]-i):
        possible_durations.append(i)
        break

for i in range(race[0]):
    if race[1] < i*(race[0]-i):
        possible_durations.append(i)
        break


print(len(range(possible_durations[1], possible_durations[0])) + 1)
print(datetime.now() - startTime)
