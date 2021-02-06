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
print("What is the powerhouse of the cell?")

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
a = "mitochondria"
if(a == "mitochondria"):
    print("correct")
else:
    print("Incorrect, the correct answer is A")

#Ask the user question two. And store the users answer.
print("How many states comprise the United States?")

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
c = "50"
if(c == "50"):
    print("correct")
else:
    print("Incorrect, the correct answer is c")
#Ask the user question three. And store the users answer.
print("In y = mx + b, what does m stand for?")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
a = "slope"
if(a == "slope"):
    print("correct")
else:
    print("Incorrect, the correct answer is a")
#Ask the user question four. And store the users answer.
print("In English, a person, place or thing is called")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
c = "noun"
if(c == "noun"):
    print("Correct")
else:
    print("Incorrect, the correct answer is c")
    
#Calculate the percentage the user got. And store it in a variable called p
p = score / 4
#Print out the users score: "You got a [score]/4. Or a [p]%."
print("you got a [score]/4")
