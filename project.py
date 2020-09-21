""" PYTHON IFE RETAIL MARKET PROJECT """

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
        stock.append({"item": row[0], "quantity": row[1], "price": row[2]})
    stock_file.close()

    stock = [ {"item": row[0], "quantity": int(row[1]), "price": int(row[2])}
            for row in [ [cell.strip("'") for cell in line.strip().split(', ')]
            for line in open(filepath, 'r')] ]

    return stock

