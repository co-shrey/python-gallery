logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
name_bidd={}
end=False
def bi(record):
    highest_bid=0
    for i in record:
        amount=record[i]
        if amount>highest_bid:
            highest_bid=amount
            winner=i
    print(f"the winner is {winner} with bid amount of {highest_bid}")

while not end:
   name=input("your name:")
   bid=int(input("your bid:"))

   name_bidd[name]=bid
   s_con=input("are u want to bid agin?yes or no:")
   if s_con=="no":
       end=True
       bi(name_bidd)

