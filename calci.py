logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return  n1-n2
def multi(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

set_operations={
    "+":add,
    "-":sub,
    "*":multi,
    "/":divide,
}

def calculations():
    num1=float(input("enter your first number:"))


    for i in set_operations:

        print(i)
    end=True
    while end:
       operation = input("pick an opeartion:")
       num2=float(input("enter your next number:"))

       calcu=set_operations[operation]
       final_ans=calcu(num1,num2)
       print(f"final answer is {final_ans}")

       should_continue=input("type yes or no or start from new:")
       if should_continue=="yes":
          num1=final_ans
       elif should_continue=="no":
          end=False
       else:
           calculations()



calculations()