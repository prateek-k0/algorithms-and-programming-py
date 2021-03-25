import threading
import time

def first():
   print(threading.currentThread().getName() + str(' is starting \n '))
   time.sleep(5)
   print(threading.currentThread().getName() + str(' is exiting \n '))
   return

def second():
   print(threading.currentThread().getName() + str(' is starting \n '))
   time.sleep(5)
   print(threading.currentThread().getName() + str(' is exiting \n '))
   return

def third():
   print(threading.currentThread().getName() + str(' is starting \n '))
   time.sleep(5)
   print(threading.currentThread().getName() + str(' is exiting \n '))
   return

if __name__ == '__main__':
   t1=threading.Thread(target=first,args=())
   t2=threading.Thread(target=second,args=())
   t3=threading.Thread(target=third,args=())

   t1.start()
   t2.start()
   t3.start()
   t1.join() #join statements can be left too, since the effect is same as with including them
   t2.join()
   t3.join()

