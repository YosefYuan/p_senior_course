
x = [-3,-4, -5,1, 2, 3, 4, 5]
y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]
print(y)