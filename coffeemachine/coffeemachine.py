"""Coffemachine project by Oliinyk Maksym"""
import sys

class CoffeeMachine:
    """First Class Using"""
    def __init__(self):
        #stock recourses of mine coddemachine
        self.recourses = {
            "water": 400,
            "milk": 540,
            "coffee_beans": 120,
            "cups": 9,
            "money": 550,
        }

    pass

def check_resources(check_water, check_coffee, check_milk):
    """Use that thing if you want check resources"""
    global water, milk, coffee_beans, cups
    if check_water > water:
        print("Sorry there is not enough water.")
        return False
    elif check_coffee > coffee_beans:
        print("Sorry there is not enough water.")
        return False
    elif check_milk > milk:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True

def main_choice():
    """Our main desk"""
    menu = 'Write action (buy, fill, take, remaining, exit):'
    choice = None

    while choice != "exit":
        choice = input(menu).strip()

        if choice == "buy":
            buy_section()

        elif choice == "fill":
            fill_section()

        elif choice == "take":
            take_section()

        elif choice == "remaining":
            rem_section()

def buy_section(water, milk, beans, cups, money):
    """Old but gold way to buy something"""
    weapon_of_choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
    water_espresso = 250
    coffee_beans_espresso = 16
    money_espresso = 4
    water_latte = 350
    milk_latte = 75
    coffee_beans_latte = 20
    money_latte = 7
    water_cappuccino = 200
    milk_cappuccino = 100
    coffee_beans_cappuccino = 12
    money_cappuccino = 6
    if coffee_beans == '1':
        water -= water_espresso
        coffee_beans -= coffee_beans_espresso
        cups -= 1
        money += money_espresso
    elif coffee_beans == '2':
        water -= water_latte
        milk -= milk_latte
        coffee_beans -= coffee_beans_latte
        cups -= 1
        money += money_latte
    else:
        water -= water_cappuccino
        milk -= milk_cappuccino
        coffee_beans -= coffee_beans_cappuccino
        cups -= 1
        money += money_cappuccino
    print('The coffee machine has:')
    print(water, ' of water')
    print(milk, ' of milk')
    print(beans, ' of coffee_beans')
    print(cups, ' of disposable cups')
    print(money, ' of money')

def fill_section(self):
    """Smart way to fill our CoffeeMachine"""
    self.recourses['water'] += int(input("Write how many ml of water do you want to add:\n"))
    self.recourses['milk'] += int(input("Write how many ml of milk do you want to add:\n"))
    self.recourses['coffee_beans'] += int(input("Write how many grams of coffee beans do you want to add:\n"))
    self.recourses['cups'] += int(input("Write how many disposable cups of coffee do you want to add:\n"))

def take_section(self):
    """Smart way to take our money from machine"""
    print(f"I gave you {self.machine_standard['money']}")
    self.machine_standard['money'] = 0

def rem_section():
    print("Coffemachine has:")
pass