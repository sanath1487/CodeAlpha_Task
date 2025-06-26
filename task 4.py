#CodeAlpha Internship Task 4 
#Build a simple rule-based chatbot
def chatbot():
    for i in range(0,4):
        word=input("Enter your input word:")
        if word.upper()=='HELLO':
            print("Hi!")
        elif word.upper()=='HOW ARE YOU':
            print("I'm Fine, thanks!")
        elif word.upper()=="BYE":
            print("Goodbye!")
        else:
            continue
chatbot()

"""In this program, I have used the upper() function
This is because, the user might enter the input in any case 
Irrespective of the case of input, the statements will result to True and thus execute."""
        
        
