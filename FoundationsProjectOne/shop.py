####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Nour-shop"
signature_flavors = ["pumpkin","mouseroyal","oreo"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    for item in menu:
        print("- \"%s\": %s" % (item, menu[item]))

def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for item in original_flavors:
        print("-\"%s\" " % item)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for item in signature_flavors:
        print("-\"%s\" " % item)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!

    if order.lower() in menu:
        return True
    elif order.lower() in original_flavors:
        return True
    elif order.lower() in signature_flavors:
        return True
    else:
        return False



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    order = input("Please type your order as spelled on the menu, type \"exit\" when you're done \n")
    while order.lower() != "exit":
        if is_valid_order(order):
            order_list.append(order)
        else:
            print("This item is not on the menu, please choose other item, or type \"exit\" to end the order")

        order = input()

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        return True
    else:
        return False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for item in order_list:
        if item in menu:
            total +=  menu[item]
        elif item in original_flavors:
            total += original_price
        elif item in signature_flavors:
            total += signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    total = get_total_price(order_list)
    print()
    print("Your order is: ")
    # your code goes here!
    for item in order_list:
        print ( "\"%s\"" % item )

    
    print ("Total Price = \"%s\" " % get_total_price(order_list))
    
    if accept_credit_card(total):
        print ("This order eligible for credit card")
    else:
        print ("Sorry!! This order is not eligible for credit card, you're total price must reach 5:00KD")
