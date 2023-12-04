file = []
with open('day_3_input.txt') as f:
    file = f.read()
file = file.split('\n')

numbers = []
result = 0

for row in range(len(file)):
    current_num = ''
    spots = []
    for char in range(len(file[row])):
        if file[row][char].isnumeric():
            current_num += file[row][char]
            spots.append([row,char])
        else:
            if current_num:
                numbers.append([spots, current_num])
                current_num = ''
                spots = []
        if current_num and char == len(file[row])-1:
            numbers.append([spots, current_num])
            current_num = ''
            spots = []

for row in range(len(file)):
    for char in range(len(file[row])):
        if file[row][char] == '*':
            number_count = 0
            part_nums = []
            for number in numbers:
                if (
                       [row-1,char] in number[0]
                    or [row+1,char] in number[0]
                    or [row,char-1] in number[0]
                    or [row,char+1] in number[0]
                    or [row-1,char-1] in number[0]
                    or [row-1,char+1] in number[0]
                    or [row+1,char-1] in number[0]
                    or [row+1,char+1] in number[0]
                    ):
                    number_count += 1
                    part_nums.append(int(number[1]))
            if len(part_nums) == 2:
                result += part_nums[0] * part_nums[1]

print(result)

