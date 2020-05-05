items = int(input("Enter number of items: "))
if items == 1:
    print("$ 10.95")
else:
    total = 2.95 * (items - 1) + 10.95
    print("${0: 0.2f}".format(total))
