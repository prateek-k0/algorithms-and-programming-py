class one():
   def __init__(self,a):
      self.a=a
      return
   
   def disp(self):
      print(self.a)
      return

class two():
   class_object = one(10)
   
   def __init__(self,a):
      self.object_1 = one(a)
      

object_2=two(5)
object_2.object_1.disp()

two.class_object.disp()


