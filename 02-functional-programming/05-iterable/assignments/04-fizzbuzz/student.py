def fizzbuzz():
    current = 1
    while True:
        if current % 3 == 0 and current % 5 == 0:
            yield "fizzbuzz"
        elif current % 3 ==0:
            yield "fizz"
        elif current % 5 == 0:
            yield "buzz"
        else:
            yield str(current)
        current += 1