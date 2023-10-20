import random 
playing=True 
balance = 100
print("---Coin Flip---")
print( " Flip a coin. If you guessed the right side, you get double of what you bet. ")
print(" continue to bet until you loose. ")
while playing == True:
    Heads=False
    Tails=False
    side =0 
    print("you have " + str(balance) + " points")
    
    bet=input("how much do you want to bet?")
    balance -= int(bet)
    side = random.randint(1,3)
    if side == int(1):
        Outcome= str("Heads")
    else:
        Outcome= str("Tails")
    guess= input(str("which side do you choose? Heads or Tails?"))
    if guess == "Heads":
        guess= int(1)
    else:
        guess= int(2)
    print(" The Side was " + str(Outcome))
    if side == int(1):
        if int(guess) == int(side):
            print("You Won! you got " + str(int(bet)*2) + " points")
            balance += (int(bet)*2)
        else: 
            print("You lost. You lost " + str(bet) )
    else:
        if int(guess) == int(side):
            print("You Won! you got " + str(int(bet)*2) + " points")
            balance += (int(bet)*2)
        else: 
            print("You lost. You lost " + str(bet) )
    if balance <=0:
        playing=False
        print("You are now bankrupt")
