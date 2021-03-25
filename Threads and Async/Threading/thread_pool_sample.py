import threading
import time

class ThreadPool():

   def __init__(self):
      self.lock = threading.RLock()
      self.active=[]

   def initiate(self,name):
      with self.lock : 
         self.active.append(name)
         print('Running threads: ', self.active, sep='  ')
      return

   def kill(self,name):
      with self.lock :
         self.active.remove(name)
         print('Running threads: ', self.active, sep='  ')
      return

def scheduler(sem_lock , pool):
   print('Waiting to join . . .')
   name = threading.currentThread().getName()
   with sem_lock:    #no need to use acquire and release; it will be checked automatically
      pool.initiate(name)
      time.sleep(0.5)
      pool.kill(name)
   return

pool = ThreadPool()
sem_lock = threading.Semaphore(3)
for i in range(5):
   t1 = threading.Thread(target=scheduler, name = 'thread '+str(i), args=(sem_lock,pool))
   t1.start()
   
   

