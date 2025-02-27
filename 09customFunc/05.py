MIN_VALUE = 1
MAX_VALUE = 100

def validation_check(value):
    global MIN_VALUE, MAX_VALUE
    MIN_VALUE += value
    MAX_VALUE -= value

validation_check(10)
print(MIN_VALUE, MAX_VALUE)

