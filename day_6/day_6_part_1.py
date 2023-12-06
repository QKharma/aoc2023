file = []
with open('day_6_input.txt') as f:
    file = [' '.join(line.strip().split()) for line in f.readlines() if line.strip() != '']

file = [x.split(':')[1].strip().split(' ') for x in file]

races = [[int(file[0][i]), int(file[1][i])] for i in range(len(file[0]))]

result = []

for race in races:
    possible_durations = []
    for i in range(race[0]+1):
        if race[1] < i*(race[0]-i):
            possible_durations.append(i)

    result.append(len(possible_durations))

print(reduce(lambda x, y: x * y, result))
