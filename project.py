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

    # stock = [ {"name": row[0], "quantity": int(row[1]), "price": int(row[2])}
    #         for row in [ [cell.strip("'") for cell in line.strip().split(', ')]
    #         for line in open(filepath, 'r')] ]

    return stock


def display_items():
    """ Display available items with their unit prices """

    print('|', "ID".ljust(2), '||', "Item".ljust(30), '||', "Unit Price (#)".rjust(14), '|')
    print('='*54)
    for item_no, item in enumerate(stock, 1):
        name, quantity, price = item.values()
        if quantity > 0:
            print('|', str(item_no).ljust(2),
                    '||', name.ljust(30),
                    '||', str(price).rjust(14), '|')
    print()


# stock = read_stock("data.csv")

# display_items()

# change_detail(stock, "price")
# change_detail(stock, "quantity")

# display_items()
