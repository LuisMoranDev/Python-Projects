import random
coin = {"heads": 0, "tails": 0}


while True:
    try:
        times = int(
            input("Enter the number of times you want to flip the coin: "))

    except ValueError:
        print("Enter a value")

    else:
        break

counter = 0
flipNum = random.randint(1, 2)
while times != counter:

    if flipNum == 1:
        coin["heads"] += 1

    else:
        coin["tails"] += 1
    counter += 1
    flipNum = random.randint(1, 2)


for x, y in coin.items():
    print(x, y)
