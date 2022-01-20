MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def sufficient(order_i):
    for i in order_i:
        if order_i[i]>=resources[i]:
            print(f"sorry there is not enough {i}")
            return False
    return True
def coins():
    print("insert your coins")

    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def t_s(m_received,drink_cost):
    if m_received>=drink_cost:
        c=round(m_received-drink_cost,2)
        print(f"here is money change:{c}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("sorry not enough money")
        return False
def make_c(drink_n,order_i):
    for i in order_i:
        resources[i]-=order_i[i]
    print(f"here is your ☕ {drink_n}.enjoy!")
end=True
while end:
      choice=input("espresso/latte/cappuccino:")
      if choice=="off":
          end=False
      elif choice=="report":
          print(f"water:{resources['water']}")
          print(f"milk:{resources['milk']}")
          print(f"coffee:{resources['coffee']}")
          print(f"money:${profit}")
      else:
          drink=MENU[choice]
          print(drink)
          if sufficient(drink["ingredients"]):
              pay=coins()
              if t_s(pay,drink["cost"]):
                  make_c(choice,drink["ingredients"])
