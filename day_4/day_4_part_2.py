file = []
with open('day_4_input.txt') as f:
    file = f.read()
file = file.split('\n')

card_counts = []

for i in range(len(file)):
    card_counts.append(1)

result = 0

for idx, row in enumerate(file):
    if row:
        row = row.split('|')
        winning_numbers = row[0].strip().replace('  ', ' ').split(' ')
        numbers = row[1].strip().replace('  ', ' ').split(' ')
        matching_numbers = set(winning_numbers).intersection(numbers)
        for i in range(idx,len(matching_numbers)+idx):
            card_counts[i+1] += card_counts[idx]

print(sum(card_counts))

