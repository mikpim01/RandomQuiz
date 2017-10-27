import random

#the questions/answer dictionary
my_dict =   {
                "What is the answer to life, the universe and everything?" : "42",
                "Translate 'I have' to German." : "Ich habe",
                "Translate 'I am' to French." : "Je suis",
                "11.5 tonnes in kilograms." : "11500",
                "How many syllables are in a haiku?" : "17",
                "Translate 'Cheers!' to German." : "Prost!",
                "In the life cycle of a star the same size as our sun, what stage comes after white dwarf?" : "Black Dwarf",
                "What is the place where you find planets and stars?" : "Space",
                "How many zeros are in one googol?" : "100",
                "What does AI stand for?" : "Artificial Intelligence",
                "What is Pi rounded to 5 decimal places?" : "3.14159",
            }

#welcome message
print("Physics Mini-Quiz")
print("=======================")
print("A Python Code")

#the quiz will end when this variable becomes 'False'
playing = True

#While the game is running
while playing == True:

    #set the score to 0
    score = 0

    #gets the number of questions the player wants to answer
    num = int(input("\nType the number of questions: "))

    #loop the correct number of times
    for i in range(num):

        #the question is one of the dictionary keys, picked at random
        question = (random.choice( list(my_dict.keys())))
        #the answer is the string mapped to the question key
        answer = my_dict[question]

        #print the question, along with the question number
        print("\nQuestion " + str(i+1) )
        print(question  + "?")

        #get the user's answer attempt
        guess = input("> ")

        #if their guess is the same as the answer
        if guess.lower() == answer.lower():
            #add 1 to the score and print a message
            print("Correct!")
            score += 1
        else:
            print("Nope!")

    #after the quiz, print their final score  
    print("\nYour final score was " + str(score))

    #store the user's input...
    again = input("Enter any key to play again, or 'q' to quit.")

    #... and quit if they types 'q'
    if again.lower() == 'q':
        playing = False
