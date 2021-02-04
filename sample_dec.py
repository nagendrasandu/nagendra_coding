def wish_decorator(func):
    def inner1():
        print('before execution')
        func()
        print('after execution')
    return inner1


# @wish_decorator
def hello_decorator():
    print('good morning')
x=wish_decorator(hello_decorator)
x()
