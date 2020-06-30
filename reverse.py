def reverse(sentence):
    reverse_sentence = ''
    for x in sentence:
        reverse_sentence = x + reverse_sentence 
    return reverse_sentence




sentence = input('Enter a sentence: ')
# reverse_sentence = ''
# for x in sentence:
#     reverse_sentence = x + reverse_sentence 
# print(reverse_sentence)
print(reverse(reverse(sentence)))
print(reverse(sentence))

