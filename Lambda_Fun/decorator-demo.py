def outer():
    print("Hello from outer  Function")
    def inner():
        print("Hello from inner function")
    return inner
d=outer()
d()