logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
print(logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    c=random.choice(cards)
    return c
def score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
def comp(user_score,com_score):
    if user_score==com_score:
        return "draw"
    elif com_score==0:
        return "lose,opponent has a black-jack"
    elif user_score==0:
        return "win"
    elif user_score>21:
        return "u went beyond the limit,loose"
    elif com_score>21:
        return "opponent crossed the limit,u win!"
    elif user_score>com_score:
        return "you won"
    else:
        return "you loose!!"
user_card=[]
com_cards=[]
end=False
for i in range(2):

    user_card.append(deal_card())
    com_cards.append(deal_card())
while not end:
        user_score=score(user_card)
        com_score=score(com_cards)
        print(f"user choices are:{user_card} and score is :{user_score}")
        print(f"comp first choice is {com_cards[0]}")
        if user_score==0 or com_score==0 or user_score>21:
            end=True
        else:
            should_c=input("type y or n:")
            if should_c=="y":
                user_card.append(deal_card())
            else:
                end=True
while com_score!=0 and com_score<17:
    com_cards.append(deal_card())
    com_score=score(com_cards)
print(f"your final cards:{user_card} and your final score:{user_score}")
print(f"comp choices are:{com_cards} and final score:{com_score}")
print(comp(user_score,com_score))