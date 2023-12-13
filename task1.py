while True:
    try:
        order_amount= int(input("How many pizzas would you like to order today?:"))
        if order_amount <= 1:
            print(" Please enter a valid amount")
            continue
            break
    except ValueError:
                print("please enter a valid number to continue")
                amount = order_amount *12
                print(f"Your total will be: £{amount}")

print(f"Your current total is £{amount}, proceed to see total after discounts")
while True:
    tuesday = input("Is it Tuesday today? Yes or No? ")
    if tuesday == "yes":
        amount = amount/2
        print(f"Your new total with discount is £{amount}")
        if tuesday == "no":
            print("Unfortunately no discount can be applied this moment in time")
            break
        else: