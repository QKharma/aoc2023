file = []
with open('day_1_input.txt') as f:
    file = f.read()
file = file.split('\n')

string_to_num = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}

sum = 0

for s in file:
    print(s)
    values = {}
    for key in string_to_num:
        all_found = False
        s_copy = s
        while not all_found:
            if key in s_copy:
                cutoff = len(s) - len(s_copy)
                values[s_copy.find(key)+cutoff] = string_to_num[key]
                s_copy = s_copy[s_copy.find(key)+1:]
            else:
                all_found = True
    for idx, c in enumerate(s):
        if c.isnumeric():
            values[idx] = int(c)
    values = dict(sorted(values.items()))
    values = [value for key, value in values.items()]
    sum += int('{}{}'.format(values[0],values[-1]))
    

print(sum)
