import random
import random_word
from random_word import RandomWords #import random word generator

r = RandomWords() #Object that holds library of words

word = r.get_random_word() #Gets word
word = word.upper() #capitalise
phrase = list(word)  #turn random word into a list of characters
answer = [] #will be where we place our answers

#print(word)
print(phrase)
#appens - to answer string to realise the length of the word
for item in range(0,len(phrase)):
    answer.append('-')

#Fills in predetermined slots in the word
answer.insert(0, phrase[0])
answer.pop(1)
answer.insert(2, phrase[2])
answer.pop(3)
answer.insert(4, phrase[4])
answer.pop(5)

print('Welcome to Hangman! ')
print(answer)
print("Please choose a letter")

#for loop handles the game
for attempt in range(1,len(word) + 3): #tries equal to length of the word
    print(f'Tries left: {11 - attempt}')
    guess = input().upper() #capitalise each guess to avoid errors

    #error catching if phrase is wrong
    if phrase.__contains__(guess) is False:
        print(f"{guess} is incorrect")

    #correct answer goes through here
    elif phrase.__contains__(guess):
        print(f'{guess} is one of the letters')
        answer.pop(phrase.index(guess)) #pops a - in the answer list to be replaced with the correct guess
        answer.insert(phrase.index(guess), guess) #inserts correct guess into answer
        phrase.insert(phrase.index(guess),'-') #inserts a dash into the guess index of the correctly guessed guess
        phrase.pop(phrase.index(guess)) #pops the position of the guess to avoid double detection
        #if statement to check if the word has been guessed completely
        if answer == list(word):
            print(answer)
            print("YOU WIN")
            attempt = len(word) + 2 #sets attempts to last stage to exit for loop
            break
    print(answer)
print(word)

