old_price=[10,20,30,40,50,60,70]
rs=5
def add_price(no):
    return no+5
new_price=map(add_price,old_price)
new_price1=list(map(lambda n:n+rs,old_price))
print(new_price1)