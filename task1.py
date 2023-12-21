if __name__== '__main__':

        order_amount= int(input("How many pizzas would you like to order today?:"))
        if order_amount <= 1:
            print(" Please enter a valid amount")

elif order_amount >= 1:
    print("please enter a valid number to continue")
amount = order_amount *12
print(f"Your current total is £{amount}, proceed to see total after discounts")
if True:
    tuesday = input("Is it Tuesday today? Yes or No? ")
    if tuesday == "yes":
        amount1 = amount/2
        print(f"Your new total with discount is £{amount1}")
        if tuesday == "no":
            print("Unfortunately no discount can be applied this moment in time")
        elif tuesday == False:
            print("invalid input, please enter yes or no")

            delivery_cost = 2.50
            amount1 = (amount + delivery_cost)
            while True:
                delivery = input("Do you need delivery? Yes or No?")

                if delivery == "yes":
                    if order_amount <= 5:
                        print(f"The new total is £{delivery_cost}")
                        print(f"As more than 5 pizzas have been ordered, you get free delivery.")
                    break
                if delivery == "no":
                    print(" no delivery charge added")
                    break
                else:
                    print("enter yes or no")
                App= delivery_cost/2
            while True:
                App = input("Are you using the app today? Yes or No?")

                if delivery == "yes":
                        print(f"The new total is £{delivery_cost}")
                        print(f"As more than 5 pizzas have been ordered, you get free delivery.")
                    break

