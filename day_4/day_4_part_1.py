file = []
with open('day_4_input.txt') as f:
    file = f.read()
file = file.split('\n')

result = 0

for row in file:
    if row:
        row = row.split('|')
        winning_numbers = row[0].strip().replace('  ', ' ').split(' ')
        numbers = row[1].strip().replace('  ', ' ').split(' ')
        matching_numbers = set(winning_numbers).intersection(numbers)
        if matching_numbers:
            result += pow(2, len(matching_numbers)-1)

print(result)

