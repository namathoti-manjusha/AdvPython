import multiprocessing
res=[]
def square_num(numbers):
    global res
    for n in numbers:
        res.append(n*n)
    print("data inside the protocols {}".format(res))
if __name__=='__main__':
    numbers=[1,2,3,4,5]
    p=multiprocessing.Process(target=square_num,args=(numbers,))
    p.start()
    p.join()
    print("data inside the main process {}".format(res))