#CodeAlpha Internship Task 1 
#Create a simple text-based Hangman game where the player guesses a word one letter at a time.
l=['hello','hi','fine','welcome','thanks']
def guessword():
    j=0
    while j<=4:
        i=0 #For counting the number of incorrect guesses
        k=0 #For counting the number of correct letters guessed
        word=l[j]
        print("Word number #", j+1)
        for e in range(0,len(word)+6): #6 is added including the max number of incorrect guesses
            gletter=input("Enter the guessed letter :")
            if gletter.lower() in word: #This converts the input letter into lowercase to match with that in the list
                print("Correct guess!!\n Go for next letter")
                k+=1
                if k==len(word):
                    print("Congrats!!! All the letters of the word guessed!!\n The word is ",l[j])
                    print("Proceed to the next word")
                    break
            else:
                print("Incorrect guess!!")
                i+=1
                if i>=6:
                    print("Max limit of incorrect guesses reached\n Moving to the next word")
                    break    
        j+=1
guessword()
