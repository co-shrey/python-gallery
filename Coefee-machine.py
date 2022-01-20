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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
end=True
while end:
    choice=input("espresso/latte/cappuccino:")

    if choice == "latte" or choice == "cappuccino" or choice == "espresso":
        c = MENU[choice]
        # cost_i=c["cost"]

        # cost_i=c["cost"]
        p = c['cost']
        if resources['water'] >= c['ingredients']['water'] and resources['coffee'] >= c['ingredients']['coffee']:
            print("insert your coins")

            total = int(input("how many quarters?: ")) * 0.25
            total += int(input("how many dimes?: ")) * 0.1
            total += int(input("how many nickles?: ")) * 0.05
            total += int(input("how many pennies?: ")) * 0.01
            print(total)






            if total>=p:
                    total-=p
                    print(f"u got {choice}!enjoy!! and your remaining amount is ${total}")
                    resources['water']-=c['ingredients']['water']

                    resources['coffee'] -= c['ingredients']['coffee']


            else:
                    print("sorry!!you can't get it")
        else:
            print("sorry!amount of ingredients are not sufficient")
    elif choice == "latte" or choice == "cappuccino" or choice == "espresso" or choice=="report":
        c = MENU[choice]
        # cost_i=c["cost"]

        # cost_i=c["cost"]
        p = c['cost']
        print(f"water:{resources['water'] - c['ingredients']['water']}")
        print(f"milk:{resources['milk'] - c['ingredients']['milk']}")
        print(f"coffee:{resources['coffee'] - c['ingredients']['coffee']}")


    else:
        print(f"water:{resources['water']}")
        print(f"milk:{resources['milk']}")
        print(f"coffee:{resources['coffee']}")

    #if int(choice['cost'])>total:
            #total-=int(choice['cost'])
            #print("enjoy your drink")
        #else:
            #print("sorry you haven't that much money")
