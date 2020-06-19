def plural(word):
    if 's' != word[-1]:
        word = word + 's'
    return word 

x = input('enter word: ')
print(plural(x))

xword = input('enter word: ')
print(plural(xword))