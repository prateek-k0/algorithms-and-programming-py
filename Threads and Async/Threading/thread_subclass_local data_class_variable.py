import threading


class myclass(threading.Thread):
   thread_local_obj = threading.local()  # create an object of local class using class variable
     
   def __init__(self,name):
      threading.Thread.__init__(self)
      self.name=name

   def run(self):
      myclass.thread_local_obj.value = 1   # create a variable a specific to the thread and initialize it
      for i in range(1,6):
         print('Thread ', self.name, ' :  value = ', myclass.thread_local_obj.value, end='\n')
         myclass.thread_local_obj.value += 1
      
my_obj = myclass('1')
my_obj_two = myclass('2')

my_obj.start()
my_obj.join()

print('\n')

my_obj_two.start()
my_obj_two.join()
