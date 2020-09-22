""" Utility functions for the Retail Market Project """

def change_detail(stock, detail):
    """ Function for admin to change ptice of items """

    max_id = len(stock)  # Instead of len() being computed on each loop.
    progress = 'y'
    while progress == 'y':
        try:
            item = int(input("Enter item ID: "))
            if item < 1 or item > max_id:
                print("Invalid Item ID")
                continue
            value = input("Enter new %s: " % detail)
            if detail != "name":
                value = int(value)
                if value < 0:
                    print("Invalid %s!!" % detail)
        except ValueError:
            print("Invalid input")
            continue
        else:
            stock[item - 1][detail] = value
            print("%s of '%s' successfully changed" % (detail, stock[item - 1]["name"]))
        finally:
            progress = input(
                    "Do you want to change the %s of another item (y/n)? "
                    % detail).lower()
    print()


def add_items(stock):
    """ Adds new items to the stock """

    progress = 'y'
    while progress == 'y':
        try:
            name = input("Enter Item Name: ")
            quantity = int(input("Enter item Quantity: "))
            if quantity < 0:
                print("Invalid quantity!!")
                continue
            price = int(input("Enter Unit Price of item: "))
            if price <= 0:
                print("Invalid price!!")
                continue
        except ValueError:
            print("Invalid input")
            continue
        else:
            # Add if item doesn't already exists in stock
            for item in stock:
                if item["name"].lower() == name.lower():
                    print("'%s' already exists in stock!" % name)
                    break
            else:
                # No matching item in stock
                stock.append({"name": name, "quantity": quantity, "price": price})
                print("'%s' successfully added." % name)
        finally:
            progress = input("Do you want to add another item (y/n)? ").lower()
    print()

