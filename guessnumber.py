import random 

max_guess = 15
num_digits = int(input("How many digits you want to play with: "))
print("Welcome to the game. You'll be informed after each guess.")
print(f"Guess a {num_digits} digit number up to {max_guess} times.")
print("NOTE: Every digit is different!")

def get_secret_num():
    text = ''
    numbers_list = list(range(0, 10))
    random.shuffle(numbers_list)
    for i in range(num_digits):
        text += str(numbers_list[i])
    return text

def get_clues(guess, secret_number):
     if guess == secret_number:
         return "You guessed right!"
     text = ''
     for i in range(num_digits):
         if guess[i] == secret_number[i]:
             text += f"A correct digit is in the correct place\n"
         elif guess[i] in secret_number:
             text += "A correct digit is in the wrong place\n"
         else:
             text += "Not a correct digit\n"
     if len(text) == 0:
         return "No digit is correct"
     else:
         return text
num_guess = 0
secret_number = get_secret_num()
while True:
    guess = input("Enter your guess: ")
    while len(guess) != num_digits or not guess.isdecimal():
        guess = input("Please enter a valid value: ")
    num_guess += 1
    clues = get_clues(guess, secret_number)
    print(clues)
    if guess == secret_number:
        print(f"Total guesses: {num_guess}")
        break
    if num_guess > max_guess:
        print("You ran out of guess.")
        print(f"Answer is {secret_number}")
        break
    if guess == 'q':
        print(secret_number)
