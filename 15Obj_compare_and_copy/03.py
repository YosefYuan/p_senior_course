t1 = (1, 2, [3, 4])
t2 = (1, 2, [3, 4])

print(t1 == t2)

t1[-1].append(5)
t1 == t2
print(t1 == t2)
