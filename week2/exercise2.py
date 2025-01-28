pas = 123
guesses = 3


print(f"You can guess {guesses} times")
upas1 = int(input("Enter the password: "))

if upas1 == pas:
    print("Welcome")
else:
    guesses -= 1
    print(f"You can guess {guesses} times")
    upas2 = int(input("Enter the password: "))
    if upas2 == pas:
        print("Welcome")
    else:
        guesses -= 1
        print(f"You can guess {guesses} times")
        upas3 = int(input("Enter the password: "))
        if upas3 == pas:
            print("Welcome")
        else:
            guesses -= 1
            print("The password is incurrect! ")

# print(f"You can guess 3 times")
# upas2 = int(input("Enter the password: "))

# while upas2 != pas:
#     print("Wrong!")
#     print(f"You can guess {guesses} times")
#     upas2 = int(input("Enter the password: "))
#     guesses -= 1
#     if guesses == pas:
#         print("welcome")
#     elif guesses == 0:
#         print("You can't guess again!")
#         break

    