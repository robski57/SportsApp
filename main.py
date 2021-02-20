# Dictionary hold all of the items and the prices of each item for sale.
aList = {"hat": 19, "sweater": 32, "shirt": 27, "jacket": 50}
aList_Name = ("Hat $19, Sweater $32, Shirt 27, Jacket $50")

# Var add to hold items customer selects and the total price of everything
basket = []
total = []

# Welcome message to all who uses this app
welcome = ("Welcome to Robert's Sports app")
print(welcome)

# cashier, allows user to make a selection from the dictionary and once item has been selected it is added to the basket
# With a message that indecates the item has been added
# If item is not availbile customer will receive a error message
# and the customer is if they would like to continue shopping or quit.
# if a addtional item is selected it will be added to the basket
# is the customer chose to quit the program will show he the items she selected and total her out.
def cashier():
    print(aList_Name)
    itemName = input("Please make a selection from our list of items: ").lower()
    while itemName != "quit":
        if itemName in aList:
            basket.append(itemName)
            itemName = input("Perfect! i will add that to your basket anything else you would like to purchase?"
                             "(Type 'quit' to end )").lower()
        else:
            itemName = input("I am sorry we don't have that, is there anything else you would like?"
                             "(Type 'quit' to end)").lower()


cashier()

print(" here are all the items in your shopping cart: ", basket)

ans = input("Do you wish to add anything else? (Type yes/no)").lower()

if ans == "yes":
    cashier()
    print(" here are all the items in your shopping cart: ", basket)
    for items in basket:
        total.append(aList[items])
    amount_to_pay = sum(total)
else:
    for items in basket:
        total.append(aList[items])
    amount_to_pay = sum(total)

print("your total amount is: ", amount_to_pay)

