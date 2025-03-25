def rle_encode(data):
    if not data:
        return None
    counter = 0
    previous = None
    for character in data:
        if character == previous or previous is None:
            previous = character
            counter += 1
        else:
            yield (previous, counter)
            previous = character
            counter = 1
    yield (previous, counter)


def rle_decode(data):
    for pair in data:
        for i in range(pair[1]):
            yield pair[0]

# test = rle_encode("")
# print(next(test))
# print(next(test))
# print(next(test))