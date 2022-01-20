import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
name=["berserk","kerfuffle","mixology"]
chose=random.choice(name)


word=[]
for letter in chose:
    word+="_"

print(word)
guess_word=""
live=6
end=False
while not end:
   #while live!=7:
    guess = input("enter the letter:")
    for i in  range(len(chose)):
             letter=chose[i]
             if letter==guess:
                word[i] = letter
        #live+=1
        #print(f"remaining lives are{7-live}")
    if guess in chose:
       print(f"you guess the word:{guess}")
    print(word)
    if guess not in chose:
       print(f"you have guesses the letter:{guess},you loose a life")
       live-=1
       if live==0:
           end=True
           print("you lose")

    if "_" not in word:
        end=True
        print("you win")

    print(stages[live])
