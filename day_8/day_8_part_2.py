from datetime import datetime
import math
from functools import reduce
startTime = datetime.now()

file = []
with open('day_8_input.txt') as f:
    file = [' '.join(line.strip().split()) for line in f.readlines() if line.strip() != '']

nodes = {}
instructions = file[0]

for row in file:
    if '=' in row:
        row = row.split(' = ')
        row_name = row[0]
        row_values = row[1][1:-1].split(', ')
        nodes[row_name] = row_values

locations = [key for key, x in nodes.items() if key[2] == 'A']
step_counts = []

for location_idx, _ in enumerate(locations):
    done = False
    location_reached = 0
    step_count = 0
    while not done:
        for step in instructions:
            step_count += 1
            if step == 'L':
                locations[location_idx] = nodes[locations[location_idx]][0]
            if step == 'R':
                locations[location_idx] = nodes[locations[location_idx]][1]
            if locations[location_idx][2] == 'Z':
                location_reached += 1
                if location_reached == 2:
                    step_counts.append(step_count)
                    done = True
                else:
                    step_count = 0
                     


print(reduce(lambda x,y:(x*y)//math.gcd(x,y),step_counts))
print(datetime.now() - startTime)