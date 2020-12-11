
import random

sick_days = random.randint(0, 10)
print(sick_days)
while sick_days:
    actually_sick = bool(random.randint(0, 2))
    kinda_sick = bool(random.randint(0, 2))
    dont_feel_like_it = bool(random.randint(0, 2))
    calling_in_sick = bool(actually_sick and sick_days) or bool(kinda_sick and dont_feel_like_it and sick_days)
    print(f'Checking out if you have the right to stay home ......{calling_in_sick}')
    if calling_in_sick:
        print( f'how lucky you are!, u still have {sick_days} sick days, stay at home!' )
        sick_days -= 1
print(f'Checking out if you have the right to stay home ......{not calling_in_sick}')
print('No more sick days, Come to the Office! Now!')
