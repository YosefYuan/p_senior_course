l1 = [[1, 2], (30, 40)]
l2 = list(l1)

l1.append(100)
l1[0].append(3)

print(l1)

print(l2)

l1[1] += (50, 60)

print(l1)

print(l2)