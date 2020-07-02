import random 
answer = random.randint(0,100)
guess = -1

while guess != answer: 
    guess = int(input('Enter number between 0 and 100 here: '))
    if guess > answer:
        print('lower ⬇️')
    elif guess < answer:
        print('higher ⬆️')
    else:
        print('Winner!🌈')    