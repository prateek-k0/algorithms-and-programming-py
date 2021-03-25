import threading
import time

def f1():
  
   print(threading.currentThread().getName() + str(' is executing... \n'))
   n=input("Waiting for user input:\n ")
   print('Exiting.....\n' )
   return

def f2():
   print(threading.currentThread().getName() + str(' is executing... \n'))
   print('before')
   
   time.sleep(5)
   print('after delay')
   print('2nd thread exitin\n')
   return

if __name__=='__main__' :
   t1=threading.Thread(name='first_thread' , target=f1, args=() )
   t2=threading.Thread(name='second_thread', target=f2, args=() )
   
   t1.start()
  # t1.join() #remove this, and second thread starts executing during I/O of the first thread
   t2.start()

