file = []
with open('day_2_input.txt') as f:
    file = f.read()
file = file.split('\n')

games_sum = 0

for idx, row in enumerate(file):
    red, blue, green = 0,0,0
    row = row.split(':')[1]
    row = row.split(';')
    for i in range(len(row)):
        row[i] = row[i].split(',')
    for pull in row:
        for color in pull:
            color = color.strip()
            number = int(color.split(' ')[0])
            if 'red' in color and number > red:
                red = number
            if 'green' in color and number > green:
                green = number
            if 'blue' in color and number > blue:
                blue = number
    print(red, green, blue)
    games_sum += red*green*blue
            

print(games_sum)

