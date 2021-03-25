import threading
import time
from threading import Semaphore as sl

sem_lock = sl(2)

# creation of a lock object that allows atmost 2 threads to share a resource simultaneously

def task1():
   resource_1(threading.currentThread().getName())
   resource_2(threading.currentThread().getName())
   
def task2():
   resource_2(threading.currentThread().getName())
   resource_1(threading.currentThread().getName())


def resource_1(name): 
   sem_lock.acquire()  
   print(name + ' is executing resource 1 . . . . ', end='\n')
   time.sleep(3)
   print(name + ' is exiting resource 1. . . . ', end='\n\n')
   sem_lock.release()

def resource_2(name):
   sem_lock.acquire() 
   print(name + ' is executing resource 2 . . . . ', end='\n')
   time.sleep(3)
   print(name + ' is exiting resource 2. . . . ', end='\n\n')
   sem_lock.release()


if __name__ == '__main__' :
   t1 = threading.Thread(target=task1, name="Thread 1")
   t2 = threading.Thread(target=task2, name="Thread 2")

   t1.start()
   t2.start()

   t1.join()
   t2.join()
