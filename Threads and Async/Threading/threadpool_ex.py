import threading
import time
from threading import Semaphore as sl
from threading import RLock as rl

class threadpool(threading.Thread) :
   thread_count = 0
   thread_list = []
   s_lock = sl(2)
   r_lock = rl()

   def __init__(self):
      super(threadpool,self).__init__()   
      return
   
   def run(self):
      print(threading.currentThread().getName() + "Waiting for execution . . . . . ")
      with threadpool.s_lock :
         self.initiate()
         time.sleep(1)
         self.destruct()
      print(threading.currentThread().getName() + " is leaving the pool . . . . . ")
      return

   def initiate(self):
      print(threading.currentThread().getName() + " is beginning to execute . . . . . ")
      with threadpool.r_lock :
         threadpool.thread_count += 1
         threadpool.thread_list.append(threading.currentThread().getName())
      print("Number of threads currently executing: ", threadpool.thread_count)
      return

   def destruct(self):
      print(threading.currentThread().getName() + " is stopping to execute . . . . . ")
      with threadpool.r_lock :
         threadpool.thread_count -= 1
         threadpool.thread_list.remove(threading.currentThread().getName())
      print("Number of threads currently executing: ", threadpool.thread_count)
      return


for i in range(3):
   t1 = threadpool()
   t1.start()
   
   
