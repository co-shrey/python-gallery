rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
your_choice=int(input(" 0 for rock,1 for paper or 2 for scissors:"))
if your_choice>=3 or your_choice<0:
  print("invalid")
else:
  if your_choice==0:
    print(rock)
  elif your_choice==1:
    print(paper)
  elif your_choice==2:
    print(scissors)
  computor_choice=random.randint(0,2)
  print(computor_choice)
  if computor_choice==0:
    print(rock)
  elif computor_choice==1:
    print(paper)
  elif computor_choice==2:
    print(scissors)


  if your_choice==0 and   computor_choice==2:
    print("you win")
  elif your_choice==0 and computor_choice==1:
    print("computor wins and you lost")
  elif your_choice==computor_choice:
    print("toss")
  elif your_choice==1 and computor_choice==2:
    print("computor win and you lost")
  elif your_choice==2 and computor_choice==1:
     print("you win")
  elif your_choice==2 and computor_choice==0:
    print("computor wins and you lost!")
  elif your_choice==1  and computor_choice==0:
    print("you win")
