from itertools import groupby
def rle_encode(data):
    for key, group in groupby(data):
        yield (key, len(list(group)))

def rle_decode(data):
    for pair in data:
        for i in range(pair[1]):
            yield pair[0]
test = rle_encode("abbc")
print(next(test))
print(next(test))
print(next(test))