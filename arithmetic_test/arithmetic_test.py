import random

def test_2_lvl(counter):
    for j in range(5):
        num3 = random.randint(11, 29)
        print(num3)
        answer = input(">")

        while not answer.lstrip('-').isdigit():
            answer = input("Incorrect format.\n>")

        answer = int(answer)

        if answer == num3 ** 2:
            print("Right!")
            counter += 1
        else:
            print("Wrong!")

    print(f"Your mark is {counter}/5")
    return counter

def test_1_lvl(counter):
    for i in range(5):
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operator = random.choice(["+", "-", "*"])

        print(num1, operator, num2)
        answer = input(">")

        while not answer.lstrip('-').isdigit():
            answer = input("Incorrect format.\n>")

        answer = int(answer)

        if operator == "+":
            if answer == num1 + num2:
                print("Right!")
                counter += 1
            else:
                print("Wrong!")

        elif operator == "-":
            if answer == num1 - num2:
                print("Right!")
                counter += 1
            else:
                print("Wrong!")

        elif operator == "*":
            if answer == num1 * num2:
                print("Right!")
                counter += 1
            else:
                print("Wrong!")

    print(f"Your mark is {counter}/5")
    return counter

def save_results(name, counter, level, level_desc):
    edited_text = f"{name}: {counter}/5 in level {level} ({level_desc}).\n"

    with open('results.txt', 'a') as file:
        file.write(edited_text)
        print("Your results have been saved to results.txt")

def main():
    level = input("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n>")

    while level not in ["1", "2"]:
        level = input("Incorrect format.\n>")

    counter = 0

    if level == "1":
        counter = test_1_lvl(counter)
    else:
        counter = test_2_lvl(counter)

    save_results_input = input("Would you like to save your result to the file? Write yes/no\n>")

    if save_results_input.lower() == "yes":
        name = input("Enter your name:\n>")
        if level == "1":
            level_desc = "simple operations with numbers 2-9"
        else:
            level_desc = "integral squares of 11-29"

        save_results(name, counter, level, level_desc)
    else:
        print("Your results have not been saved.")

if __name__ == "__main__":
    main()
