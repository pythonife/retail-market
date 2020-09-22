""" PYTHON IFE RETAIL MARKET PROJECT """

from utils import *

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


def display_items(stock):
    """ Display available items with their unit prices """

    disp_format = "| {:>2} || {:<30} || {:>14} |"
    print('='*58)
    print(disp_format.format("ID", "Item", "Unit Price (#)"))
    print('='*58)
    for item_no, item in enumerate(stock, 1):
        name, quantity, price = item.values()
        if quantity > 0:
            print(disp_format.format(item_no, name, price))

    print('='*58)
    print()


my_stock = read_stock("data.csv")

display_items(my_stock)

make_purchase(my_stock, {i: 100 for i in range(10, 21)})

# display_items(my_stock)
