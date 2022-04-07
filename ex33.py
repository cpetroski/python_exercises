

def test_function(r, y):
    i = 0
    numbers = []

    while i < r:
        print(f"At the top i is {i}")
        numbers.append(i)

        i= i + y
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


        print("The numbers: ")

    for num in numbers:
        print(num)

test_function(37, 4)
