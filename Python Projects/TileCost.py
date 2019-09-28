def tileCost(width, height):
    area = width * height
    tile = 4
    while True:
        try:
            cost = float(input("Enter the cost per tile: "))

        except ValueError:
            print("Must be an integer ")

        else:

            if cost < 0:
                print("Cost must be greater than 0")
            else:
                break

    if area < tile:
        print("$ %.2f" % cost)
    else:
        price = cost * (area / tile)
        print("$ %.2f" % price)


tileCost(10, 10)
