from operator import le
import random


wordList = ['ali', 'javad', 'amirreza','sadeq', 'farideh', 'amirhossein', 'mohsen', 'reza']


word = random.choice(wordList)
true_guess = []
life = 5
while(True):
    for item in range(len(word)):
        if word[item] in true_guess:
            print(word[item], end='')
        else:    
            
            print("-",end ="")

    for i in range(len(word)):
        foundAllLetters = True
        if word[i] not in true_guess:
            foundAllLetters = False
            break
    if foundAllLetters :
        print('\nyou won the game')
        break
    print('\nplease enter char')
    char = input()
    if len(char) == 1 :
        if char in word :
            true_guess.append(char)
            print('yes')
        else:
            life -=1
            print('you lost one life')
            print('life exist', life)
        if(life == 0) :
            print('bakhti!!!')
            break    
    else:
        print('please enter char')
            