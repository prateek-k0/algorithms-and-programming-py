import threading
import time
from threading import Lock as l

lock_obj=l()
x=0

class mythread(threading.Thread):
   def __init__(self, name, counter):
      threading.Thread.__init__(self)
      self.name=name
      self.counter=counter

   def run(self):
      print("\nStarting " + str(self.name), end='\n')
      lock_obj.acquire()
      myfunc(self.name,self.counter)
      lock_obj.release()
      print("Exiting the thread..... \n")
      

def myfunc(name,counter):  
   global x
   for i in range(counter):  
      x+=1
   print(str(name) + ": value of x = ",x,end='\n' )
   return


t1=mythread("thread1",7)
t2=mythread("thread2",5)

#t2.start()
#t1.start()



