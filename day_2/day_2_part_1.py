file = []
with open('day_2_input.txt') as f:
    file = f.read()
file = file.split('\n')

impossible_games = []

for idx, row in enumerate(file):
    impossible = False
    row = row.split(': ')[1]
    row = row.split('; ')
    for i in range(len(row)):
        row[i] = row[i].split(', ')
    for pull in row:
        for color in pull:
            if 'red' in color and int(color.split(' ')[0]) > 12:
                impossible = True
            if 'green' in color and int(color.split(' ')[0]) > 13:
                impossible = True
            if 'blue' in color and int(color.split(' ')[0]) > 14:
                impossible = True
    if not impossible:
        impossible_games.append(idx+1)

print(sum(impossible_games))

