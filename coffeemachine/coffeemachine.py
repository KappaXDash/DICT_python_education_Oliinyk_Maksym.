"""Coffemachine project by Oliinyk Maksym"""
class CoffeMachine:
    """First time using class"""
    def __init__(self):
        """stock recourses of mine coddemachine"""
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9

    def main_choice(self):
        """That thing can accept your action"""
        done = False
        while not done:
            choice = input('Write action:\n 1-buy\n 2-fill\n 3-take\n 4-remaining\n 5-exit\n:')
            if choice == "1":
                CoffeMachine.buy(self)
            elif choice == "2":
                CoffeMachine.fill(self)
            elif choice == "3":
                CoffeMachine.take(self)
            elif choice == "4":
                CoffeMachine.available(self)
            elif choice == "5":
                done = True
            else:
                print("invalid choice")

    def return_to_menu(self):
        """That thing can comeback you"""
        print()
        self.main_choice()

    def buy(self):
        """That thing can accept your choice"""
        drink = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu\n:")
        if drink == "back":

            return
        elif drink == '1':
            if CoffeMachine.enough_not_enough(self, 250, 0, 16):
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
        elif drink == '2':
            if CoffeMachine.enough_not_enough(self, 350, 75, 20):
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
        elif drink == '3':
            if CoffeMachine.enough_not_enough(self, 200, 100, 12):
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
        else:
            print('invalid choice')
            return CoffeMachine.buy(self)

    def enough_not_enough(self, needed_water, needed_milk, needed_coffee):
        """Use this thing to see if there are enough resources"""
        if self.water < needed_water:
            print('Sorry, not enough water!')
            return False
        if self.milk < needed_milk:
            print('Sorry, not enough milk!')
            return False
        if self.beans < needed_coffee:
            print('Sorry, not enough beans!')
            return False
        if self.cups < 1:
            print('Sorry, not enough cups\n')
            return False
        print('I have enough resources, making you a coffee!\n')
        print("\n")
        return True

    def available(self):
        """Use that thing if you want check resources"""
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(f"$ {self.money} of money")
        print("\n")

    def fill(self):
        """Use that thing if you want add recourses"""
        self.water += int(input("Write how many ml of water you want to add:\n"))
        self.milk += int(input("Write how many ml of milk you want to add:\n"))
        self.beans += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.cups += int(input("Write how many disposable coffee cups you want to add:\n"))
        print("\n")
        self.return_to_menu()

    def take(self):
        """Show text of taking process"""

        print()
        print(f'I gave you {self.money} griven')
        print("\n")
        self.money = 0


if __name__=="__main__":
    '''Commands for class'''
    coffe = CoffeMachine()
    coffe.main_choice()
