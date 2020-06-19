x = input('Enter a word here: ')
con_suffix = 'ay'
vowel_suffix = 'yay'
first_letter = x[0]
VOWELS = 'aeiou'

if first_letter in VOWELS:
    print(x + vowel_suffix)
else:
    print(x[1:] + first_letter + con_suffix)
