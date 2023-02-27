from threading import *
class Myclass(Thread):
    def demo(self):
        print("HCL")
    def run(self):
        print("Hello From THREAD")
        self.demo()
obj=Myclass()
obj.start()