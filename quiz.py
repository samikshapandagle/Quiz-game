print("Welcome to my quize")

play = input ("Do you want to play?")
score = 0

if play != "yes":
    quit()

print("okayy! Let's play :")

answer = input ("whst does CPU stands for?")
if answer == "central processing unit":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    
answer = input ("What is the capital of France?")
if answer == "Paris":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    
answer = input ("Which planet is known as the Red Planet?")
if answer == "Mars":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    
answer = input ("What is the chemical symbol for water?")
if answer == "H2O":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    
answer = input ("Which element has the atomic number 1?")
if answer == "Hydrogen":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    
print("You got " +  str(score)  + " questions correct!")
print("You got" +str((score/5) * 100)+ "%.")
