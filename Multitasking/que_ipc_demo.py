import multiprocessing
def square_num(num,q):
    for n in num:
        q.put(n*n)
def cube(number,q):
    for n in number:
        q.put(n*n*n)
if __name__=='__main__':
    numbers=[1,2,3,4,5]
    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=square_num,args=(numbers,q))
    p2=multiprocessing.Process(target=cube,args=(numbers,q))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    while q.empty() is False:
        print(q.get())