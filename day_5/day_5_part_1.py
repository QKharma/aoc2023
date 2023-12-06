file = []
with open('day_5_input.txt') as f:
    file = [line.strip() for line in f.readlines() if line.strip() != '']

seeds = [int(x) for x in file[0].split(':')[1].strip().split(' ')]

tables = []
table = []

for row in file[1:]:
    if 'map' in row:
        if table:
            tables.append(table)
            table = []
    else:
        table.append([int(x) for x in row.split(' ')])
tables.append(table)

for i in range(len(tables)):
    for s in range(len(seeds)):
        for j in range(len(tables[i])):
            destination_start = tables[i][j][0]
            source_start = tables[i][j][1]
            range_length = tables[i][j][2]
            if seeds[s] in range(source_start, source_start + range_length):
                seeds[s] = seeds[s] - (source_start - destination_start)
                break

print(seeds)
print(min(seeds))


