letter = input('enter a letter: ').lower()
vowels = 'aeiou'
if letter in vowels:
    print('it is a vowel')
elif letter == 'y':
    print('sometimes y is a consonate, sometimes y is a vowel')
else:
    print('consonate')
