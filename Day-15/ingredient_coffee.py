MENU = {
        "espresso":{
           "ingredients":{
                "water" : 50,
                "coffee" :18,       
           },
           "cost" : 1.5,
        },

    
        "latte":{
           "ingredients":{
                "water" : 200,
                "milk" : 150,
                "coffee" :24,       
           },
        "cost" : 2.5,
        
    },

        "cappuccino":{
           "ingredients":{
                "water" : 50,
                "milk" :100,
                "coffee" :24,       
           },
           "cost" : 3.00
    },
}
    
resources ={
    "water" : 300,
    "milk" : 200,
    "coffee" :100,
}



def is_resource_available(ingredients_available):
    """Returns True if the given ingredients are available False if ingredients are not available"""
    # print(ingredients_available)
    is_enough = True
    for item in ingredients_available:
        if ingredients_available[item] >= resources[item]:
            print(f"Water is not available that much {item}")
            is_enough = False
    return is_enough



def process_coin():
    """Returns the total amount of coin"""
    print("Please insert coin")
    total = int(input("How many quarters ? : ")) * .25
    total += int(input("How many dimes ? : ")) * .1
    total += int(input("How many nickles ? : ")) * .05
    total += int(input("How many pennies ? : ")) * .01
    return total



profit = 0
# payment , cost
def is_transaction_successful(money_received , drink_cost):
    """Rturn True when transaction is successful and False when not enough money"""
    if money_received > drink_cost:
        change = round(money_received - drink_cost , 2)
        print(f"Here is {change} money in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False



def make_coffe(drink_name , order_ingedient):
    for item in order_ingedient:
        resources[item] -=  order_ingedient[item]
    print(f"Here is your {drink_name} ")



is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == 'off':
        is_on = False

    elif choice == 'report':
        print(f"water : {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee :{resources['coffee']}")
    
    else:
        order = MENU[choice]
        # print(order)
        if is_resource_available(order["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment , order["cost"]):  
                make_coffe(choice, order["ingredients"])