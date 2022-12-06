import random


def game():
    print("HANGMAN""\nThe game will be available soon.")
    words = ['python', 'java', 'javascript', 'php']

    picked = random.choice(words)

    print('The Word has', len(picked), 'letters')

    right = ['_'] * len(picked)
    wrong = []

    def update():
        for x in right:
            print(x, end=' ')
        print()

    update()

    while True:

        guess = input("Input a letter:>")

        if guess in picked:
            index = 0
            for i in picked:
                if i == guess:
                    right[index] = guess
                index += 1
            update()

        else:
            if guess not in wrong:
                wrong.append(guess)
            else:
                print('You already guessed that')
            print(wrong)
        if len(wrong) > 8:
            print('You lost!')
            print('I picked', picked)
            break
        if '_' not in right:
            print('You survived!')
            break


def menu():
    print("Start")
    print("Exit")


menu()
user_input = input("Please write your choice \"start\" or \"exit\" -->")
while user_input != "user_input":
    if user_input == "start":
        game()
        pass
    elif user_input == "exit":
        exit()
    else:
        print("Incorrect input!")

    menu()
    user_input = input("Please write your choice \"start\" or \"exit\" -->")