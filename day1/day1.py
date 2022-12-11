'''Counting highest calories from elves based on .txt with whitespaces'''
with open('day1_input.txt', encoding='utf-8') as f:
    calories = f.readlines()
    elves_calories = []
    tmplist = []
    for index, line in enumerate(calories):
        if line == "\n" or index == len(calories) -1:
            elves_calories.append(tmplist.copy())
            del tmplist[:]
        else:
            tmplist.append(int(line.strip()))

elves_sum_calories = []

for i in elves_calories:
    elves_sum_calories.append(sum(i))

#stage 1 result
print(max(elves_sum_calories))

sorted_elves_sum_calories = sorted(elves_sum_calories, reverse=True)
#stage 2 result
print(sum(sorted_elves_sum_calories[0:3]))
