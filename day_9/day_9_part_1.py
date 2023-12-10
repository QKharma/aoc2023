file = []
with open('day_9_input.txt') as f:
    file = [' '.join(line.strip().split()) for line in f.readlines() if line.strip() != '']

file = [x.split(' ') for x in file]

result = 0

for idx, sequence in enumerate(file):
    subsequences = [[int(x) for x in sequence]]
    while sum([abs(x) for x in subsequences[-1]]) != 0:
        new_subsequence = []
        for idx, num in enumerate(subsequences[-1][:-1]):
            new_subsequence.append(subsequences[-1][idx+1] - num)
        subsequences.append(new_subsequence)

    subsequences.reverse()

    for idx, sequence in enumerate(subsequences[:-1]):
        subsequences[idx+1].append(subsequences[idx+1][-1] + subsequences[idx][-1])

    result += subsequences[-1][-1]

print(result)