import pymongo
import threading
from pymongo import MongoClient
cl=MongoClient("mongodb+srv://josetellis2018:dHmjZHB5MZgPsH0f@cluster0.ghrj9wz.mongodb.net/?retryWrites=true&w=majority")
db=cl['hcl_data']
col=db['train_data']
lock=threading.Lock()
def read():
    result=col.find({},{"_id":0})
    for r in result:
        print(r)
def update_tkt(seats):
#acquire the lock before accessing the shared resource
    lock.acquire()
    try:
        #access the shared resource
        r=col.find_one({},{"_id":0})
        avail=r["No_of_seats"]
        if seats<=avail:
            avail=avail-seats
        else:
            print("seats are not available")
        up_qury={"$set":{"No_of_seats":avail}}
        fil_cd={"Train_no":12345}
        col.update_one(fil_cd,up_qury)
    finally:
        # release the lock after accessing the shared resource
        lock.release()
#update_tkt(10)
read()