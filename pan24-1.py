
def a(b):
    return b[1]

l1 = [(2, 2), (3, 4), (4, 1)]

l1.sort(key = a)

print(l1)