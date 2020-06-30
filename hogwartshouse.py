import random 
Gtraits = ['courage', 'bravery', 'chivalry']
Htraits = ['loyalty', 'justice', 'hard work']
Rtraits = ['intelagence', 'wisdom', 'learning']
Straits = ['ambition', 'cunning', 'resoursefulnesss']
print('Here are the house traits!:')
alltraits = Gtraits + Htraits + Rtraits + Straits
random.shuffle(alltraits)
for trait in alltraits:
    print(trait)

usertrait= input('Enter your trait: ').lower()
if usertrait in Gtraits:
    print('You are a Gryffindor!' )
elif usertrait in Htraits:
    print('You are a Hufflepuff!')
elif usertrait in Rtraits:
    print('You are a Ravenclaw!')
elif usertrait in Straits:
    print('You are a Sytherin!' )
else:
    print('You are a Muggle!!')


