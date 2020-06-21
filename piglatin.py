def piglatinafy(word):
    if '' == word:
        return ''
    else:
        con_suffix = 'ay'
        vowel_suffix = 'yay'
        first_letter = word[0]
        VOWELS = 'aeiou'

        if first_letter in VOWELS:
            return word + vowel_suffix
        else:
            return word[1:] + first_letter + con_suffix

x = input('Enter a sentence here: ')
print(x.split(' '))
answer = '' 
for word in x.split(' '):
    print(piglatinafy(word))
    answer += ' ' + piglatinafy(word)
print(answer.strip(' ') + '!')


