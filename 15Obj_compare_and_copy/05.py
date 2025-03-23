l1 = [1, 2, 3]

l2 = l1[:]

print(l1 == l2)

print(l1 is l2)

l2[0] = 100

print(l1)
print(l2)