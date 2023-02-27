from concurrent.futures import ThreadPoolExecutor
import threading
def task():
    print("Executing Task")
    res=0
    i=0
    for i in range(200):
        res+=1
        print("{}".format(res))
        print("Task Executed {}".format(threading.current_thread()))
def main():
    executer=ThreadPoolExecutor(max_workers=3)
    task1=executer.submit(task)
    task2=executer.submit(task)
if __name__=="__main__":
    main()