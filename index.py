import random

# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess the number 1 and {x}: '))
#         if guess < random_number:
#             print('Sorry number is less')
#         elif guess > random_number:
#             print('Sorry number is high')
    
#     print(f'Wao, you guess the number {random_number}')


def computer_guess(x):
    low = 1
    high = x
    guessing = ''
    while guessing != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        guessing = input(f'is {guess} too high, too low or Correct ?? ').lower()
        if guessing == 'h':
            high = guess - 1
        elif guessing == 'l':
            low = guess + 1
    print(f'Yay! computer guess the number {guess} correctly')

computer_guess(10)