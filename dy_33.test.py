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
digit_1 = t + r + u + e

l = names_lower.count(word2[0])
o = names_lower.count(word2[1])
v = names_lower.count(word2[2])
e = names_lower.count(word2[3])
digit_2 = l + o + v + e

love_score = int(str(digit_1) + str(digit_2))
if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos')
elif love_score > 40 and love_score < 50:
    print(f'Your score is {love_score}, you are alright together')
else:
    print(f'Your score is {love_score}')


