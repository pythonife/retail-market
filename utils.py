""" Utility functions for the Retail Market Project """

def change_detail(stock, detail):
    """ Function for admin to change ptice of items """

    max_id = len(stock)
    progress = 'y'
    while progress == 'y':
        try:
            item = input("Enter item ID: ")
            if detail != "name":
                item = int(item)
            if item < 1 or item > max_id:
                print("Invalid Item ID")
                continue
            value = int(input("Enter new %s: " % detail))
        except ValueError:
            print("Invalid input for '%s'!!" % detail)
            continue
        else:
            stock[item - 1][detail] = value
            print("%s of '%s' successfully changed" % (detail, stock[item - 1]["name"]))
        finally:
            progress = input(
                    "Do you want to change the %s of another item (y/n)? "
                    % detail).lower()
    print()

