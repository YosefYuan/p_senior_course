import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*a, **b):
        print('wrapper of decorator')
        func(*a, **b)
    return wrapper

@my_decorator
def greet(name):
    print(f'Hello {name}!')

print(greet.__name__)

greet('name')