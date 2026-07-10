print("Welcome to the quiz and test your knowledege")
input("Press Enter to continue...")
print()
print("This quiz wont be easy")
print("If you got 5/5 you are equivalent to einstein!!!!!!!!")
input("Press Enter to continue...")
print()
score = 0
A = "27/10000"
B = "27/10"
C = "3/11"
D = "None of the above"
print("1. Which of the following will give the value 0.27272....?")
print(f'1. {A}')
print(f'2. {B}')
print(f'3. {C}')
print(f'4. {D}')
response = input("Pease enter the correct number: ")
if response == "3":
    print("correct answer!!!!")
    score += 1
else:
    print("I wish you were smarter😔")
    print(f'Correct answer:{C}')
print()
A = "Saturn"
B = "Neptune"
C = "Jupiter"
D = "Uranus"
print('2. Which of the following planets does NOT have rings?')
print(f'1. {A}')
print(f'2. {B}')
print(f'3. {C}')
print(f'4. {D}')
response1 = input("Pease enter the correct number: ")
if response1 == "3":
    print("Proud of you")
    score += 1
else:
    print("This is common sense!")
    print(f'Correct answer: {C}')
print()
A = "8/3"
B = "8/15"
C = "32/3"
D = "25/40"
print("3. What is the value of 2/5 + 4/15 + 2?")
print(f'1. {A}')
print(f'2. {B}')
print(f'3. {C}')
print(f'4. {D}')
response2 = input("Pease enter the correct number: ")
if response2 == "1":
    print("Legendary solve!🙌")
    score += 1 
else:
    print("Have you passed 7th?")
    idiot = input("Yes or No?: ").lower()
    if idiot == "yes":
        print("I doubt it")
    else:
        print("You better get the next questions right")
print()

A = "Milky way"
B = "Andromeda galaxy"
C = "Nicolas galaxy"
D = "Archimedes galaxy"
print("What is the name of our neighbouring galaxy?")
print(f'1. {A}')
print(f'2. {B}')
print(f'3. {C}')
print(f'4. {D}')
response3 = input("Pease enter the correct number: ")
if response3 == "2":
    print("Bravo!!!")
    score += 1
else:
    print("Better luck next time😔")
    print(f'Correct answer: {B}')
print()
A = "32"
B = "64"
C = "128"
D = "512"
print("whats the cube of 8?")
print(f'1. {A}')
print(f'2. {B}')
print(f'3. {C}')
print(f'4. {D}')
response4 = input("Pease enter the correct number: ")
if response4 == "4":
    print("That's correct!!!")
    score += 1
else:
    print("You made a calculation mistake!")
    print(f'Correct answer: {D}')
print()

input("Press Enter to see results: ")
print("-------Your Results-------")
print(f'You scored {score}/5')
print()
if score == 5:
    print("Well done, you are equivalent to einstien")
elif score == 4:
    print("Almost perfect!!")
else:
    print("I suggest you should repeat school")
print("-------The End-------")