<<<<<<< HEAD
"""Program for sharing common costs"""
import random
import sys

print("Enter the number of friends joining (including you): ")
    # Python program to take integer input  in Python
"""input size of the list"""
number_of_friends = int(input())

if number_of_friends <=0:
    print('No one is joining for the party')
    sys.exit(0)
=======
import random



print("Enter the number of friends joining (including you): ")
    # Python program to take integer input  in Python

    # input size of the list
number_of_friends = int(input())

if number_of_friends <=0:
    print('No one is joining for the party'); exit(0)
>>>>>>> ccee955781c3e215789a8531dea6dbb99952669e

print("Enter the name of every friend (including you), each on a new line:")
friend_names_list = {}
for i in range(number_of_friends):
    input_person = input("> ")
friend_names_list.update({f"{input_person}": 0})

<<<<<<< HEAD
input_amount = int(input("Enter the total amount\n> "))

lucky_man = input("Do you want to use the ""Who is lucky?"" feature? Write yes/no:" "\n> ")
choice_lucky = random.choice(list(friend_names_list))
if lucky_man == "yes":
    number_of_friends -= 1
    print(f"{choice_lucky} is the lucky one!")
else:
    print("No one is going to be lucky")

amount_person = round((input_amount / number_of_friends), 2)
for key in friend_names_list:
=======

input_amount = int(input("Enter the total amount\n> "))



lucky_man = input("Do you want to use the ""Who is lucky?"" feature? Write yes/no:" "\n> ")
choice_lucky = random.choice([key for key in friend_names_list.keys()])

if lucky_man.lower() == "yes":
        number_of_friends -= 1
        print(f"{choice_lucky} is the lucky one!")
else:
        print("No one is going to be lucky" "\n");

amount_person = round((input_amount / number_of_friends), 2)
for key in friend_names_list.keys():
>>>>>>> ccee955781c3e215789a8531dea6dbb99952669e
    if key == choice_lucky and lucky_man.lower() == 'yes':
        friend_names_list[key] = 'is the lucky one!'
    else:
        friend_names_list[key] = amount_person

<<<<<<< HEAD
print(friend_names_list)
=======
print(friend_names_list)
>>>>>>> ccee955781c3e215789a8531dea6dbb99952669e
