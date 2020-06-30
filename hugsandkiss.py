def letter_count(words, letter):
    count = 0 
    for x in words:
        if x == letter:
            count = count + 1
    return count 

x = input('enter kisses and hugs: ')
hugs = letter_count(x, 'o') 
kisses = letter_count(x, 'x')

print('This is how many hugs: ' + str(hugs) + ' This is how many kisses: ' + str(kisses) )
