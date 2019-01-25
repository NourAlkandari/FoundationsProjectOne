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
cupcake_shop_name = "yummyy"
signature_flavors = ["pumbkin", "orange", "carrot"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print("Our menu")
    for item in menu:
        print("-%s, (%s KWD)" % (item, menu[item]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for item in original_flavors:
        print ("-%s " % (item))


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for item in signature_flavors:
        print ("-%s" % item)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
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
    print ("What's your order? Enter the exact spelling of the item you want. Type 'exit' to end your order.")
    order = input()
    while order.lower() != "exit":
        if is_valid_order(order):
            order_list.append(order)
        order = input()


    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    
    if total >= 5:
        return True
    else:
        return False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for order in order_list:
        if order.lower() in menu:
            total += menu[order.lower()]
        elif order.lower() in original_flavors:
            total += original_price
        elif order.lower() in signature_flavors:
            total += signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    for order in order_list:
        print ("-%s"% order)
    print ("That's will be KWD: %s" % get_total_price(order_list))
    print ("Thank you for shopping at yummyy")
