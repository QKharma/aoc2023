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

destination_reached = False
location = 'AAA'
step_count = 0

while not destination_reached:
    for step in instructions:
        step_count += 1
        if step == 'L':
            location = nodes[location][0]
        if step == 'R':
            location = nodes[location][1]
        if location == 'ZZZ':
            destination_reached = True
            break

print(step_count)