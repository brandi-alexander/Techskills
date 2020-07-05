def piglatinafy(word):
    if '' == word:
        return ''
   
    else:
        con_suffix = 'ay'
        vowel_suffix = 'yay'
        first_letter = word[0]
        VOWELS = 'aeiou'
        if  word[-1] in ',.;!?':
            punctuation = word[-1]
            word = word[:-1]
        else:
            punctuation = ''

        if first_letter in VOWELS:
            return word + vowel_suffix + punctuation

        else:
            return word[1:] + first_letter + con_suffix + punctuation 

x = input('Enter a sentence here: ')
print(x.split(' '))
answer = '' 
for word in x.split(' '):
    print(piglatinafy(word))
    answer += ' ' + piglatinafy(word)
print(answer.strip(' ') + '!')


