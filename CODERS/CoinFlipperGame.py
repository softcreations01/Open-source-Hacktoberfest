import random

def print_instructions():
    print("---Coin Flip---")
    print("Flip a coin. If you guess the right side, you double your bet.")
    print("Continue to bet until you lose or choose to quit.")

def get_bet(balance):
    while True:
        bet_str = input(f"How much do you want to bet (0 to quit, balance: {balance})?")
        try:
            bet = float(bet_str)
        except ValueError:
            print("Please enter a valid bet (a number).")
            continue

        if bet < 0:
            print("Please enter a positive bet amount.")
        elif bet == 0:
            return 0
        elif bet > balance:
            print("You cannot bet more than your balance. Try again.")
        else:
            return bet

def play_round(balance):
    side = random.choice(["Heads", "Tails"])
    guess = input("Which side do you choose? Heads or Tails?").lower()
    bet = get_bet(balance)
    
    if bet == 0:
        return balance, True

    balance -= bet

    if guess == side.lower():
        print(f"The coin landed on {side}. You won {bet * 2} points!")
        balance += bet * 2
    else:
        print(f"The coin landed on {side}. You lost {bet} points.")

    return balance, False

def main():
    balance = 100
    rounds = 0
    print_instructions()

    while balance > 0:
        rounds += 1
        print(f"Round {rounds}")
        balance, quit_game = play_round(balance)

        if quit_game:
            break
    if balance ==0:
        print("You are bankrupt")
    else:
        print("You chose to quit")
    print(f"You played {rounds} rounds and have {balance} points remaining.")

if __name__ == "__main__":
    main()
