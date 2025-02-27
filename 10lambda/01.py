square = lambda x: x ** 2
print(square(3))


list = [(lambda x: x ** 2)(x) for x in range(10)]

print(list)