import random 
rolling=True 
while rolling == True:
    number=random.randrange(1,7)
    print("You rolled a " + str(number) + "!!!")
    again=input("do you want to continue? Say 'NO' to quit")
    if again == "NO":
        rolling= False
