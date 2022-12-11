'''Counting sum of priorities from rucksack items'''
with open('day3_input.txt', encoding='utf-8') as f:
    rucksacks_items = [line.rstrip() for line in f.readlines()]

#stage 1 
sum_of_priorities = 0
for item in rucksacks_items:
    first_compartment = item[:int(len(item)/2)]
    second_compartment = item[int(len(item)/2):]
    error_item = list(set(first_compartment) & set(second_compartment))[0]
    if error_item.islower() is True:
        sum_of_priorities += (ord(error_item)-96)
    else:
        sum_of_priorities += (ord(error_item)-38)
print(sum_of_priorities)

#stage 2
badge_item_group = []
count = 0 
number_of_group = 0
sum_of_priorities_badge_items = 0
for index, item in enumerate(rucksacks_items):
    badge_item_group.append(item)
    count += 1
    if count == 3:
        count = 0 
        badge_item = list(set(badge_item_group[0+number_of_group]) & set(badge_item_group[1+number_of_group]) & set(badge_item_group[2+number_of_group]))[0]
        number_of_group += 3
        if badge_item.islower() is True:
            sum_of_priorities_badge_items += (ord(badge_item)-96)
        else:
            sum_of_priorities_badge_items += (ord(badge_item)-38)
print(sum_of_priorities_badge_items)
