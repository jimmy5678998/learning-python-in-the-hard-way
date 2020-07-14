from sys import argv

script, a, b = argv


def numbersloop(a, b):
    i = 0
    numbers = []

    while i < a:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + b
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


def numbersforloop(a, b):
    print()
    print("Here is numbers for for-loops")
    numbers = []
    for i in range(0, a, b):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i + b}")

    print("The numbers: ")

    for num in numbers:
        print(num)

numbersloop(int(a), int(b))
numbersforloop(int(a), int(b))



