'''
Created on Feb 6, 2021

The Objective of this program is to quiz the user on basic high school
trivia. 
 1) What is the powerhouse of the cell?
        A) mitochondria B) nucleus C) ribosome
    2) How many states comprise the United States?
        A) 13 B) 45 C) 50
    3) In y = mx + b, what does m stand for?
        A) slope B) output C) I don't understand math
    4) In English, a person, place or thing is called:
        A) verb B) adjective C) noun

@author: ITAUser
'''
#Make a variable called score to keep track of the correct answers. And set
#it to 0.
score = 0

#Ask the user question one. And store the users answer.
print("What is the power house of the cell?")
ansOne = input("ENTER A LETTER: A) mitochondria B) nucleous C) ribosome")

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if(ansOne.upper() == "A"):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is A")

#Ask the user question two. And store the users answer.
print("How many states comprise the United States?")
ansTwo = input("ENTER A LETTER: A) 13 B) 45 C) 50")

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if(ansTwo.upper() == "C"):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is C")

#Ask the user question three. And store the users answer.
print("In y = mx + b, what does m stand for?")
ansThree = input("A) slope B) output C) I don't understand math")

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if(ansThree.upper() == "A"):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is A")

#Ask the user question four. And store the users answer.
print("In English, a person, place or thing is called?")
ansFour = input("A) verb B) adjective C) noun")

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if(ansFour.upper() == "C"):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is C")

#Calculate the percentage the user got. And store it in a variable called p
p = score / 4

#Print out the users score: "You got a [score]/4. Or a [p]%."
print("You got a " + str(score) + "/4. Or a " + str(p) + "%.")
