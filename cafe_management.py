# Define The Menu of Restaurant/ Cafe
try:
    menu = {
        "Pizza" : 150,
        "Pasta" : 80,
        "Burger" : 60,
        "Coffee" : 40,
        "Chowmin" : 40,
        "Icecream" : 50
    }
    print("-"*50)
    print("Hello Welcome to Cafe!")
    print("-"*50)
    print ("Pizza : Rs 150\nPasta : Rs 80\nBurger : Rs 60\nCoffee : Rs 40\nChowmin : Rs 40\nIcecream : Rs 50" )

    '''for key, value in menu.items():
        print(f"{key} : Rs. {value}")
    '''
    print("-"*50)

    '''order_total variable ---> user order Rs added in this 80+70+ automatically added initial value set =0'''

    order_total = 0

    item1 = input("Enter the Name of Item want to Order?").strip().title() # Make 1st Letter Capital

    if item1 in menu:
        order_total += menu[item1] #Update item Rs 0 + item Rs
        print(f"Your Item {item1} has been added to your Order.")

    else:
        print("Sorry, Item is not available.")


    anoter_item = input("Do you want to Order another Item? (Yes/No)").strip().lower()
    '''
    .strip()
    Purpose: Removes any leading or trailing whitespace from a string.
    ---------------------------------
    .lower()
    Purpose: Converts all characters in the string to lowercase.
    '''

    if anoter_item == "yes":
        item_2 = input("Enter the Name of 2nd Item you want to Order?").strip().title() # Make 1st Letter Capital
        if item_2 in menu:
            order_total += menu[item_2] # Add new price
            print(f"Your Item {item_2} has been added to your Order.")
        else:
            print(f"Sorry, {item_2} is not available.")
    print("-"*50)
    print("Total amount you have to pay is Rs. ", order_total)
    print("-"*50)


except Exception as e:
    print("Something went wrong:", e)

finally:
    print("Thank You! For Your Order. Have a Nice Day!")
