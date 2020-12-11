# 3a

group_of_people = ['Alex', 'Eliot', 'Veronica', 'Lucy', 'Wouter', 'Bart']
first_chars = [s[0]for s in group_of_people]
# print(first_chars)

numbers = list(range(100))
sum = sum(numbers)
print(sum)


#3b


print(group_of_people)

# for statement
new_group = []
for s in group_of_people:
    if s.istitle() or s.islower():
        new_group.append(s.upper())
print(new_group)

""" met een list comprehension: in een lijn kan ik de  4 lijnen van de for statement vervangen om het zelfde resultaat 
te krijgen zonder een nieuw list te creeren"""

group_of_people = [s.upper() for s in group_of_people if(s.istitle() or s.islower())]
print(group_of_people)


#3c

list_0_9 = list(range(10))
list_matrix = [list_0_9 for n in range(10)]
print(list_matrix)
