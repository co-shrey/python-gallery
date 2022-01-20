logo='''
 _      _____ _     ____  ____  _      _____   _____  ____    _____ _     _____ ____  ____  _  _      _____   _      _     _      ____  _____ ____    _____ ____  _      _____
/ \  /|/  __// \   /   _\/  _ \/ \__/|/  __/  /__ __\/  _ \  /  __// \ /\/  __// ___\/ ___\/ \/ \  /|/  __/  / \  /|/ \ /\/ \__/|/  _ \/  __//  __\  /  __//  _ \/ \__/|/  __/
| |  |||  \  | |   |  /  | / \|| |\/|||  \      / \  | / \|  | |  _| | |||  \  |    \|    \| || |\ ||| |  _  | |\ ||| | ||| |\/||| | //|  \  |  \/|  | |  _| / \|| |\/|||  \  
| |/\|||  /_ | |_/\|  \_ | \_/|| |  |||  /_     | |  | \_/|  | |_//| \_/||  /_ \___ |\___ || || | \||| |_//  | | \||| \_/|| |  ||| |_\\|  /_ |    /  | |_//| |-||| |  |||  /_ 
\_/  \|\____\\____/\____/\____/\_/  \|\____\    \_/  \____/  \____\\____/\____\\____/\____/\_/\_/  \|\____\  \_/  \|\____/\_/  \|\____/\____\\_/\_\  \____\\_/ \|\_/  \|\____\
                                                                                                                                                                              
'''
import random
easy_level=10
hard_level=5
print(logo)
def check(guess_number,answer,turns):
    if guess_number>answer:
        print("too high")
        return turns-1
    elif guess_number<answer:
        print("too low")
        return turns-1
    else:
        print("correct guess!!you win")
def d_level():
    level = input("choose a difficulty level hard or easy:")
    if level == "easy":
        return easy_level
    else:
        return hard_level


answer=random.randint(1,100)
def game():
    print("I'm thinking the number bertween 0 and 100")
    print(f"actual ans is:{answer}")
    turns=d_level()

    guess_number=0
    while guess_number!=answer:
        print(f"you have {turns} turns")
        guess_number=int(input("enter your number:"))
        turns=check(guess_number,answer,turns)
        if turns==0:
            print("you loose!game stopped")
            return
        elif guess_number!=answer:
            print("guesss again")
game()