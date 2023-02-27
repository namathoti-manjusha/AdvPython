def decor(func):
    def inner(name):
        if name=="hcl":
            print("hello hcl")
        else:
            func(name)
        return inner
def wish(name):
    print("hello",name)
wish("wipro")
wish("hcl")