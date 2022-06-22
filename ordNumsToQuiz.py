#readMe
#intended to read a text file of ordinal numbers and convert it into a quiz
#user can choose the number of questions to take
#program shows the user if their answer is correct or not and displays the correct answers at end
#user can choose to take a quiz again or display answers of last quiz taken

import random

#readTextFile function
def readFile():
    
    #open the file for read access
    inFile=open("quiz_questions.txt","r")

    #create empty list to store questions
    questions=[]
                
    #loop file data while there is a line of data to read
    for line in inFile:

        #creates a list based on comma split from line read
        lineList=line.split(",")

        #iterate through 
        for i in range(len(lineList)):
            questionItem=lineList[i]
            text=""
            for number in questionItem.split():
                text+=chr(int(number))
            lineList[i]=text

        #append to questions list    
        questions.append(lineList)

    #close file
    inFile.close()

    #return list with questions
    return questions

#introduction function
#this is the greeting to the user
def intro():

    #prints program message to user
    print("This program has a set of 25 questions")

    #variable to save the # of questions user wants to take
    userNumOfQuestions=input("Enter # of questions you wish to answer(2-25)>>")

    #this conditional statement makes sure that the user enters a valid number to display the
    #desired amount of quiz questions
    while userNumOfQuestions.isdigit() != True:
        userNumOfQuestions=input("Please enter a valid number (2-25):")

    x=int(userNumOfQuestions)

    #makes sure number is appropriate. this conditional statement can actually be combined with the above while loop to avoid redundancy
    while x < 2 or x > 25:
        x=input("Please enter a number between (2-25):")

        while x.isdigit() != True:
            x=input("Please print a valid number between (2-25):")
        x=int(x)
        

    return int(x)
    #returns userNumOfQuestions


def randomQuestions(questionsList, numQuestionsWant):
    
    randomQuestionsList=[]
    
    for i in range(numQuestionsWant):
        j=random.randint(0,len(questionsList)-1)

        #this loops make sure the same question doesnt get added twice
        while questionsList[j] not in randomQuestionsList:
            randomQuestionsList.append(questionsList[j])

    #returns the list with randomized questions 
    return randomQuestionsList                                         

#function takes the random quiz as a parameter
def displayQuestions(quiz):
    
    #empty list to store
    #users answer for future use
    userAnswerList=[]

    #list of valid choices user can enter
    realAnswers=["A","B","C","D"]

    #traverses through the quiz list to display quiz onto console
    for list in quiz:
        print(list[0])
        print("A:",list[1])
        print("B:",list[2])
        print("C:",list[3])
        print("D:",list[4])

        userAnswer=input("Your answer>>")
        userAnswer=userAnswer.upper()

        #checks if answer is a valid entry
        while userAnswer not in realAnswers:
            print("Enter a valid choice A, B, C, or D")
            userAnswer=input("Your answer>>")
            userAnswer=userAnswer.upper()
        userAnswerList.append(userAnswer)

        if(list[5]==userAnswer):
            print("Correct")
            print("----------------------------------------------------------")
        else:
            print("Incorrect")
            print("----------------------------------------------------------")

    return userAnswerList

#this function compares the users answers to the correct answer to count the number of correct answers
def checkAnswers(quiz, userAnswers):

    i=0
    count=0

    for item in quiz:
        if item[5]==userAnswers[i]:
            count+=1
        i+=1
                
    return count

#this function serves at the end of the quiz to ask user for what action to do next
#can start new quiz, see the answers of last quiz or quit
def endOfQuiz(quiz, userAnswers):

    options=["n","q","a"]

    print("Enter 'n' to start a new quiz")
    print("Enter 'a' to see questions and answers to the last quiz")
    userChoice=input("Enter 'q' to quit>>")

    userChoice.lower()

    while userChoice not in options:
        userChoice=input("Enter a valid response>>")
        userChoice.lower()

    if userChoice=="n":
        main()
    elif userChoice=="a":
        i=0
        for item in quiz:
            print(item[0])
            print("The correct answer is:",item[5])
            print("A.",item[1])
            print("B.",item[2])
            print("C.",item[3])
            print("D.",item[4])
            if userAnswers[i]==item[5]:
                print("Your answer:",userAnswers[i])
                print("You got this answer right")
                print("----------------------------------------------------------")
            else:
                print("Your answer:",userAnswers[i])
                print("You got this answer wrong")
                print("----------------------------------------------------------")
            i+=1
        endOfQuiz(quiz, userAnswers)
    else:
        print("Thank you have a nice day!")
        
#main driver function to call every function at the appropiate step necessary
def main():
    userInputNum = intro()
    questionsList = readFile()

    quiz=randomQuestions(questionsList, userInputNum)

    userAnswers=displayQuestions(quiz)

    score=checkAnswers(quiz, userAnswers)
    print("You got a total of",score,"answer(s) correct.")
    print(score,"/",len(userAnswers))

    endOfQuiz(quiz,userAnswers)

main()




       





    


    




    
