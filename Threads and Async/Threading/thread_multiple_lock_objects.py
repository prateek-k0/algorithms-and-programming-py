import threading
import time
from threading import RLock as rl


l1 = rl()
l2 = rl()

#Each lock object represents different critical sections (resources) 
#Like, for 2 resources, we need 2 locks, hence we defined 2 lock objects l1 and l2

def task1():
   resource_1(threading.currentThread().getName())
   resource_2(threading.currentThread().getName())
   
def task2():
   resource_2(threading.currentThread().getName())
   resource_1(threading.currentThread().getName())


def resource_1(name): 
   l1.acquire()  # l1 serves a lock for resource 1
   print(name + ' is executing resource 1 . . . . ', end='\n')
   time.sleep(3)
   print(name + ' is exiting resource 1. . . . ', end='\n\n')
   l1.release()

def resource_2(name):
   l2.acquire() # l2 serves a lock for resource 2
   print(name + ' is executing resource 2 . . . . ', end='\n')
   time.sleep(3)
   print(name + ' is exiting resource 2. . . . ', end='\n\n')
   l2.release()



if __name__ == '__main__' :
   t1 = threading.Thread(target=task1, name="Thread 1")
   t2 = threading.Thread(target=task2, name="Thread 2")

   t1.start()
   t2.start()

   t1.join()
   t2.join()
