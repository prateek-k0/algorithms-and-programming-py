import threading
import time

class mythread(threading.Thread):

    def __init__(self,name,v):
        threading.Thread.__init__(self)
        self.local_obj = threading.local()      # create an object of local class using instance variable
        self.name = name
        self.value = v

    def run(self):
        self.local_obj.value = self.value     # create a variable a specific to the thread and initialize it
                                                             #however, this statement must be used only in run function
        for i in range(5):
            self.local_obj.value += 1
            print(self.name,' : value = ',  self.local_obj.value)
            time.sleep(0.5)


my1 = mythread("Thread 1",6)
my2 = mythread("Thread 2", 16)

my1.start()
my1.join()

print()

my2.start()
my2.join()
