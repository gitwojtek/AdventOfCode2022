'''Operations on stacks - part 1 and part 2 have to be run separately'''
import re 
stacks = []
start_of_stack = 0
end_of_stack = 4
for number_of_stack in range(9):
    stack = []
    for i, row in enumerate(open('day5_input.txt', encoding='utf-8')):
        row = row[start_of_stack:end_of_stack]
        for letter in re.finditer(r'\w', row):
            stack.append(letter.group())
        if i == 8:
            stack.pop()
            organized_stack = list(reversed(stack))
            break
    start_of_stack += 4
    end_of_stack += 4
    stacks.append(organized_stack)

#part 1
for i, row in enumerate(open('day5_input.txt', encoding='utf-8')):
    if 'move' in row:
        number_of_elements = int(re.findall(r'\d+', row)[0])
        idx_from = int(re.findall(r'\d+', row)[1]) - 1
        idx_to = int(re.findall(r'\d+', row)[2]) - 1 
        changing_part = stacks[idx_from][-(number_of_elements):]
        stacks[idx_to] = stacks[idx_to] + (list(reversed(changing_part)))
        stacks[idx_from] = stacks[idx_from][0:len(stacks[idx_from])-number_of_elements]
print(stacks)

#part 2 
for i, row in enumerate(open('day5_input.txt', encoding='utf-8')):
    if 'move' in row:
        number_of_elements = int(re.findall(r'\d+', row)[0])
        idx_from = int(re.findall(r'\d+', row)[1]) - 1
        idx_to = int(re.findall(r'\d+', row)[2]) - 1 
        changing_part = stacks[idx_from][-(number_of_elements):]
        stacks[idx_to] = stacks[idx_to] + (changing_part)
        stacks[idx_from] = stacks[idx_from][0:len(stacks[idx_from])-number_of_elements]
print(stacks)