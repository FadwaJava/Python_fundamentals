
def list_manipulation(list_to_work, command, location, value=0):
    if command == 'remove' and location == "end":
        print(list_to_work.pop())
    elif command == 'remove' and location == "beginning":
        print(list_to_work[0])
        list_to_work.remove(list_to_work[0])
    elif command == 'add' and location == 'beginning':
        list_to_work.insert(0, value)
        print(list_to_work)
    elif command == 'add' and location == 'end':
        list_to_work.insert(len(list_to_work), value)
        print(list_to_work)
    else:
        print("no list_manipulation asked")


list_manipulation([1, 2, 3], 'remove', 'end')
list_manipulation([1, 2, 3], 'remove', 'beginning')
list_manipulation([1, 2, 3], 'add', 'beginning', 20)
list_manipulation([1, 2, 3], 'add', 'end', 30)
list_manipulation([1, 2, 3], 'add', 'end')









