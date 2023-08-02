# Instructions
# You are going to write a program that tests the compatibility between two people.  
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 
# For Love Scores **less than 10** or **greater than 90**, the message should be:
# Your score is **x**, you go together like coke and mentos."` 
# For Love Scores **between 40** and **50**, the message should be:
# Your score is **y**, you are alright together."`
# Otherwise, the message will just be their score. e.g.:
# Your score is **z**."`
# e.g. 
# name1 = "Angela Yu"`
# name2 = "Jack Bauer"`
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3
# Love Score = 53
# Print: "Your score is 53."
# Example Input 1

# name1 = "Kanye West"
# name2 = "Kim Kardashian"
# Example Output 1
# Your score is 42, you are alright together.
# Example Input 2

# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"
#  Example Output 2
# Your score is 73.
# e.g. When you hit **run**, this is what should happen:  

# ![](https://cdn.fs.teachablecdn.com/nfSILIPSNaIOwWhPR5vr)

# The testing code will check for print output that is formatted like one of the lines below:
"Your score is 47, you are alright together."
"Your score is 125, you go together like coke and mentos."
"Your score is 54."

# Score Comparison

# Not sure you're getting the correct score for the exercise? Use this table to check your code's score against mine.

# | Name 1 | Name 2 | Score |
# | --- | --- | --- |
# Catherine Zeta-Jones | Michael Douglas |99
# Brad Pitt |	Jennifer Aniston	| 73
# Prince William	| Kate Middleton	| 67
# Angela Yu	| Jack Bauer	| 53
# Kanye West	| Kim Kardashian	| 42
# Beyonce	| Jay-Z	| 23
# John Lennon	| Yoko Ono	| 18

# Hint

# 1. The `lower()` function changes all the letters in a string to lower case. 

# [https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python](https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python)

# 2. The `count()` function will give you the number of times a letter occurs in a string. 

# [https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string](https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string)


name1= input("please enter your name: ")
name2= input("please enter your name: ")
word1 = ['t', 'r', 'u', 'e']
word2 = ['l','o','v','e']
combined_names = name1 + name2
names_lower = combined_names.lower()
t = names_lower.count(word1[0])
r = names_lower.count(word1[1])
u = names_lower.count(word1[2])
e = names_lower.count(word1[3])
first_digit = t + r + u + e

l = names_lower.count(word2[0])
o = names_lower.count(word2[1])
v = names_lower.count(word2[2])
e = names_lower.count(word2[3])
second_digit = l + o + v + e

love_score = int(str(first_digit) + str(second_digit))
if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos')
elif love_score > 40 and love_score < 50:
    print(f'Your score is {love_score}, you are alright together')
else:
    print(f'Your score is {love_score}')


