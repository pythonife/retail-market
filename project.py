""" PYTHON IFE RETAIL MARKET PROJECT """

from utils import *  # excludes `_gain`

def read_stock(filepath):
    """ Reads stock data from a csv file
    returns a list of dicts containing the stock data

    Note: Each line of the csv file is expected to be in the form:
    "'item name', 'quantity', 'unit price'\\n"
    """

    stock_file = open(filepath, 'r')
    stock = []  # List to contain stock data

    for line in stock_file:
        line = line.strip('\n').split(', ')
        row = []
        for cell in line:
            row.append(cell.strip("'"))
        row[1:] = map(int, row[1:])
        stock.append({"name": row[0], "quantity": row[1], "price": row[2]})
    stock_file.close()

    # The same can also be achieved with a single statement using list comprehensions.

    # stock = [ {"name": row[0], "quantity": int(row[1]), "price": int(row[2])}
    #         for row in [ [cell.strip("'") for cell in line.strip().split(', ')]
    #         for line in open(filepath, 'r')] ]

    return stock


def display_items(stock, admin=False):
    """ Display available items with their unit prices (and quantity for admin) """

    if admin:
        width = 70
        disp_format = "| {:>2} || {:<30} || {:>14} || {:>8} |"
    else:
        width = 58
        disp_format = "| {:>2} || {:<30} || {:>14} |"
        
    print('=' * width)
    # The number of positional arguments to .format() can exceed
    # the number of replacement fields in the string to be formatted
    # but doing the opposite with automatic field-numbering will cause an error.
    print(disp_format.format("ID", "Item", "Unit Price (#)", "Quantity"))
    print('-' * width)
    for item_id, item in enumerate(stock, 1):
        name, quantity, price = item.values()
        if admin or quantity > 0:
            print(disp_format.format(item_id, name, price, quantity))
    print('=' * width)
    print()


def buy(stock):
    """ Start and Complete a purchase """

    if input("Do you want to see the item list (Y/N)? ").lower() == 'y':
        print()
        display_items(stock)
    else:
        print()
    purchase = {}  # to contain purchase details; {id: qty, ...}
    max_id = len(stock)  # Instead of len() being computed on each iteration.
    progress = 'y'
    while progress == 'y':
        try:
            item_id = int(input("Enter item ID: "))

            # An IndexError can never occour at the last expression here
            # by virtue of the evaluation order of boolean operator `or`.
            if item_id < 1 or item_id > max_id or stock[item_id - 1]["quantity"] == 0:
                print("Invalid Item ID")
                continue

            max_qty = stock[item_id - 1]["quantity"]
            qty_question = "Enter item Quantity (1 - {}): ".format(max_qty)
            quantity = int(input(qty_question))

            if quantity < 1:
                quantity = int(input(qty_question))
                if quantity > max_qty or quantity < 1:
                    print("Invalid Quantity!!")
                    continue
            elif quantity > max_qty:
                print("Sorry, the requested quantity is currently unavailable.\n"
                        "1. Skip item\n"
                        "2. Request all available quantity\n"
                        "3. Enter another quantity\n")

                choice = int(input("Please, Choose an option: "))
                if choice == 1:
                    continue
                elif choice == 2:
                    quantity = max_qty
                elif choice == 3:
                    quantity = int(input(qty_question))
                    if quantity > max_qty or quantity < 1:
                        print("Invalid Quantity!!")
                        continue
                else:
                    print("Wrong Input!!")
                    continue
        except ValueError:
            print("Invalid input!!")
            continue
        else:
            if item_id in purchase:
                print(
                    "This item '{}' has been selected ealier with quantity '{}'".format(
                    stock[item_id]["name"], purchase[item_id]))
                print("1. Change to new quantity\n"
                        "2. Leave with previous quantity\n")

                choice = int(input("Please, Choose an option: "))
                if choice == 1:
                    purchase[item_id] = quantity
                elif choice == 2:
                    pass
                else:
                    print("Wrong input!!\nItem quantity left unchanged")
            else:
                purchase[item_id] = quantity
        finally:
            progress = input("Do you want to buy another item (y/n)? ").lower()
            while progress != 'y' and progress != 'n':
                print("Invalid Input!!")
                progress = input("Do you want to buy another item (y/n)? ").lower()
    print()

    # An empty iterable (len() == 0) has a boolean value `False`, otherwise, `True`.
    if purchase:
        total_amount = make_purchase(stock, purchase)
        update_stock(stock, purchase)
        add_gain(total_amount)
    else:
        print("You didn't select any items")
    print("Thanks for shopping with us!!!\n")


my_stock = read_stock("data.csv")
display_items(my_stock)

buy(my_stock)
# amount = make_purchase(my_stock, {i: 100 for i in range(10, 21)})
# update_stock(my_stock, {i: 121 for i in range(10, 21)})
# add_gain(amount)
view_gain()

display_items(my_stock, True)
