def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()

    return wrapper

def greet():
    print('Hello, world!')

greet = my_decorator(greet)
greet()