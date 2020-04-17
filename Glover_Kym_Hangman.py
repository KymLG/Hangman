#importing the time module
import time

#welcoming the user
name = input("Hey there, What is your name? ")

print ("Hello, " + name, "Fancy a game of hangman?!")

print ("")

#wait for 1 second
time.sleep(1)
# import random to randomly select a word from wordlist file
import random
print ("Time to start guessing, you get 7 chances...")
time.sleep(0.5)
# here we set the word list
with open("word_list.txt") as word_list:
    word = random.choice(word_list.readlines())

random.choice (word_list)
for item in word_list:
    if item in word_list:
        continue
    else:
        word_list(item)

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 7

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in wordlist   
    for char in word_list.txt:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print (char) 

        else:
    
        # if not found, print a dash
            print ("*",    ) 
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("Congratulations you win")

    # exit the script
        break              

    print

    # ask the user go guess a character
    guess = input("Please enter your guess:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the wordlist
    if guess not in word_list.txt:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print ("Wrong")    
 
    # how many turns are left
        print ("You have", + turns, 'more guesses' )
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print ("You Lose")       
