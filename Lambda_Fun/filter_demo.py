l=[5,60,45,55,65,75,190]
def demo_fun(n):
    if n>=50:
        return True
    else:
        return False
data=list(filter(demo_fun,l))
print(data)