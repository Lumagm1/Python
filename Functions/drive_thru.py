# Write code below 💖

def get_item(x):
    if x == 1:
        return '🍔 Cheeseburger'
    elif x == 2:
        return '🍟 Fries'
    elif x == 3:
        return '🥤 Soda'
    elif x == 4:
        return '🍦 Ice Cream'
    elif x == 5:
        return '🍪 Cookie'
    else:
        print("You didnt select an appropiate item")
        return

def welcome():
    menu = [
        '1)🍔 Cheeseburger',
        '2)🍟 Fries',
        '3)🥤 Soda',
        '4)🍦 Ice Cream',
        '5)🍪 Cookie'
    ]
    
    print(menu)

def input_():
    selection = int(input("Select your item: "))
    return selection

welcome()
print(get_item(input_()))