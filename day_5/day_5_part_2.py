from datetime import datetime
startTime = datetime.now()

file = []
with open('day_5_input.txt') as f:
    file = [line.strip() for line in f.readlines() if line.strip() != '']

seeds = [int(x) for x in file[0].split(':')[1].strip().split(' ')]
seed_ranges = []

for i in range(0,len(seeds),2):
    seed_ranges.append(range(seeds[i], seeds[i]+seeds[i+1]))

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
    new_seed_ranges = []
    seed_ranges_to_remove = []
    for s in range(len(seed_ranges)):
        for j in range(len(tables[i])):
            destination_start = tables[i][j][0]
            source_start = tables[i][j][1]
            range_length = tables[i][j][2]
            source_range = range(source_start, source_start + range_length)
            overlapping_range = range(max(seed_ranges[s][0], source_range[0]), min(seed_ranges[s][-1], source_range[-1]) + 1)
            if overlapping_range:
                source_destination_difference = (source_start - destination_start)
                if overlapping_range == seed_ranges[s]:
                    new_seed_ranges.append(range(seed_ranges[s][0] - source_destination_difference, seed_ranges[s][-1] + 1 - source_destination_difference))
                elif overlapping_range == source_range:
                    new_seed_ranges.append(range(seed_ranges[s][0] - source_destination_difference, overlapping_range[0] + 1 - source_destination_difference))
                    new_seed_ranges.append(range(overlapping_range[0] - source_destination_difference, overlapping_range[-1] + 1 - source_destination_difference))
                    new_seed_ranges.append(range(overlapping_range[0] - source_destination_difference, seed_ranges[s][-1] + 1 - source_destination_difference))
                elif overlapping_range[0] > seed_ranges[s][0]:
                    new_seed_ranges.append(range(seed_ranges[s][0], overlapping_range[0] + 1 ))
                    new_seed_ranges.append(range(overlapping_range[0] - source_destination_difference, overlapping_range[-1] + 1  - source_destination_difference))
                elif overlapping_range[-1] < seed_ranges[s][-1]:
                    new_seed_ranges.append(range(overlapping_range[-1], seed_ranges[s][-1] + 1 ))
                    new_seed_ranges.append(range(overlapping_range[0] - source_destination_difference, overlapping_range[-1] + 1  - source_destination_difference))
                seed_ranges_to_remove.append(s)
                break
    seed_ranges = [x for idx, x in enumerate(seed_ranges) if idx not in seed_ranges_to_remove]
    seed_ranges = seed_ranges + new_seed_ranges
                
print(min([x[0] for x in seed_ranges]))
print(datetime.now() - startTime)

