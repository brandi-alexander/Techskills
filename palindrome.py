word = input('Enter word:')
word = word.replace(' ', '')
if word[::-1] == word:
    print('Palindrome')
else:
    print('Not a Palindrome')
