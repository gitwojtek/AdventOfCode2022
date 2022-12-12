import re 
with open('day4_input.txt', encoding='utf-8') as f:
    assignments = [re.split(r',|-', line.rstrip()) for line in f.readlines()]

count = 0 
for assignment in assignments:
    if int(assignment[0]) >= int(assignment[2]) and int(assignment[1]) <= int(assignment[3]):
        count += 1
    elif int(assignment[2]) >= int(assignment[0]) and int(assignment[3]) <= int(assignment[1]):
        count += 1
print(count)

count_overlap = 0 
for assignment in assignments:
    if int(assignment[1]) >= int(assignment[2]) and int(assignment[0]) <= int(assignment[3]):
        count_overlap += 1
print(count_overlap)