#importing the time module
import time

#welcoming the user
name = input("Hey there, What is your name? ")

print ("Hello, " + name, "Fancy a game of hangman?!")

print ("")

#wait for 1 second
time.sleep(1)

print ("Time to start guessing, you get 7 chances...")
time.sleep(0.5)
# import random to randomly select a word from wordlist
import random
#here we set the word list
wordlist = ("billion")
random.choice (wordlist)
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
    for char in wordlist:      

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
    guess = input("Please enter your next guess:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the wordlist
    if guess not in wordlist:  
 
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
            
