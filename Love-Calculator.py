print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1+name2
names_lower = names.lower()
t = names_lower.count("t")
r = names_lower.count("r")
u = names_lower.count("u")
e = names_lower.count("e")
true = t+r+u+e
l= names_lower.count("l")
o= names_lower.count("o")
v= names_lower.count("v")
e= names_lower.count("e")
love= l+o+v+e
true_love= int(str(true)+str(love))
if (true_love < 10) or (true_love > 90):
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif (true_love >= 40) and (true_love <=50):
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")

