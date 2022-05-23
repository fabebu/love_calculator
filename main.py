# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1lower = name1.lower()
name2lower = name2.lower()

t1 = name1lower.count("t") + name2lower.count("t")
r1 = name1lower.count("r") + name2lower.count("r")
u1 = name1lower.count("u") + name2lower.count("u")
e1 = name1lower.count("e") + name2lower.count("e")
l1 = name1lower.count("l") + name2lower.count("l")
o1 = name1lower.count("o") + name2lower.count("o")
v1 = name1lower.count("v") + name2lower.count("v")
#e2 = name1lower.count("e") + name2lower.count("e")

first = t1 + r1 + u1 + e1
second = l1 + o1 + v1 + e1
lovescore = str(first) + str(second)
int_ls = int(lovescore)
if int_ls < 10 or int_ls > 90:
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif int_ls >= 40 and int_ls <= 50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")

