# -*- coding: utf-8 -*-
"""
Mahnoor Arif
mahnoorarif@uchicago.edu
HW1
Created on Sat Apr  6 14:38:21 2024

@author: arifm
"""

# PPHA 30537
# Spring 2024
# Homework 1

# Mahnoor arif
# coding988



# Due date: Sunday April 7th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.
### Cite: OpenAI. "ChatGPT: Python Code Generation." 2024. OpenAI, https://openai.com/chatgpt. Used for guidance purposes only for some codes##
#############
# Part 1: Introductory Python (to be done without defining functions or classes)

# Question 1.1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

#the following loop assigns 'first' position to index value 0, and so on
def index_list(first):
    index=0
    for value in first:
        print("The value at position", index, "is", value)


# Question 1.2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Microsoft" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

##citation:https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/

##'i' is a string variable that checks if a word is a plaidrome or not
def palindrome(i):
    return i==i[::-1]
       
i = 'radar', 'A man, a plan, a canal, Panama!', 'Microsoft'
if palindrome(i):
    print("It is a palindrome")
else:
    print("This isn't a palindrome")


# Question 1.3: The code below pauses to wait for user input, before assigning the user input to the
# variable. Beginning with the given code, check to see if the answer given is an available
# vegetable. If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again. Repeat until they pick a valid vegetable.
#available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']
#choice = input('Please pick a vegetable I have available: ')



available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']


while True:
    available_option = input('Yes, the following vegetable is available:',available_vegetables )
    if available_option in available_vegetables:
        print('Yes, the  vegetable is available:', available_option)
    break
else:
        print('Invalid choice. Please pick again.')


# Question 1.4: Write a list comprehension that starts with any list of strings and returns a new
# list that contains each string in all lower-case letters, unless the modified string begins with
# the letter "a" or "b", in which case it should drop it from the result.

list_countries = ["America", "Bangladesh", "Canada", "Denmark"]

##'if not' command drops countries starting with letter "a" or "b"
new_list_countries = [countries.lower() for countries in list_countries if not (countries.lower().startswith("a") or countries.lower().startswith("b"))]

print(new_list_countries)



# Question 1.5: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'WI':'Wisconsin'} 


short_names = ['IL', 'IN', 'MI', 'WI']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']
combined_dictionary= {short_names[state]: long_names[state] for state in range(len(short_names))}
print(combined_dictionary)

#############
# Part 2: Functions and classes (must be answered using functions\classes)

# Question 2.1: Write a function that takes two numbers as arguments, then
# sums them together. If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small". Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]

def list_classify(number_1, number_2):
    
    total_sum = number_1 + number_2
    
    if total_sum > 10:
        return "big"
    elif total_sum == 10:
        return "just right"
    else:
        return "small"
#following function generates results as per the classification
ordered_list = [list_classify(number_1, number_2) for number_1, number_2 in start_list]

print(ordered_list)


# Question 2.2: The following code is fully-functional, but uses a global
# variable and a local variable. Re-write it to work the same, but using one
# argument and no global variable. Use no more than two lines of comments to
# explain why this new way is preferable to the old way.


def my_func(a=10):
    b = 40
    return a + b
x = my_func()
#Explanation: By making a's value as local varibale, we can change the value of 'a' to get different results while using the same function

# Question 2.3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*). It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else print a 
# warning to the user and exit. Your function should also have a keyword 
# argument named "special_chars" that defaults to True.  If the function 
# is called with the keyword argument set to False instead, then the 
# random values chosen should not include special characters. Create a 
# second similar keyword argument for numbers. Use one of the two 
# libraries below in your solution:
#import random
#from numpy import random
  
import string
import random
#keyword argument defauting special characters and numbers to True
def password_random (length, special_chars= True, numbers= True):
    if not 8<= length <= 16:
        print("warning, try again")
        return "Error"
        #the following loop defines the applicable characters that are letters, numbers and special characters (punctuations) only
        characters_password = string.acsii_letters 
        if numbers:
          characters_password += string.digits
          if special_chars:
              characters_password += string.punctuation 
              #allows for random assignment of applicable characters in the password
              password=[]
              for _ in range (length):
                  password.append(random.choice(characters_password))
              
              return''.join(characters_password)
              
              
              
  
# Question 2.4: Create a class named MovieDatabase that takes one argument
# when an instance is created which stores the name of the person creating
# the database (in this case, you) as an attribute. Then give it two methods:
#
# The first, named add_movie, that requires three arguments when called: 
# one for the name of a movie, one for the genera of the movie (e.g. comedy, 
# drama), and one for the rating you personally give the movie on a scale 
# from 0 (worst) to 5 (best). Store those the details of the movie in the 
# instance.
#
# The second, named what_to_watch, which randomly picks one movie in the
# instance of the database. Tell the user what to watch tonight,
# courtesy of the name of the name you put in as the creator, using a
# print statement that gives all of the info stored about that movie.
# Make sure it does not crash if called before any movies are in the
# database.
#
# Finally, create one instance of your new class, and add four movies to
# it. Call your what_to_watch method once at the end.



class MovieDatabase:
    def __init__(self, mahnoor_creator):
        self.mahnoor_creator = mahnoor_creator
        self.movies =[]
        
    def add_movie(self, movie_name, movie_genre, movie_rating):
        #assigns keywords and values to dictionary movies
            self.movies.append({"name":movie_name, "genre":movie_genre, "rating": movie_rating})
        #the following code keeps the loop from crashing if movie outside the database is called#
    def what_to_watch(self):
                if not self.movies:
                    print ("Movie does not exist")
             
                else:
                    play_movie = random.choice(self.movies)
                    print(f'What to watch tonight, {self.mahnoor_creator}')
                    print(f'Movie: {play_movie["name"]}')
                    print(f'genre: {play_movie["genre"]}')
                    print(f'rating: {play_movie["rating"]}')
             
mahnoor_database_movies = MovieDatabase("mahnoor_creator")

mahnoor_database_movies.add_movie ("Saltburn", "Thriller", 5)
mahnoor_database_movies.add_movie ("The Kite Runner", "Drama", 5)
mahnoor_database_movies.add_movie ("Barbie", "Drama", 1)
mahnoor_database_movies.add_movie ("Home Alone", "Action", 3)

mahnoor_database_movies.what_to_watch()










