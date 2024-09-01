class cat:
   def __init__(self,name,age):
    self.name=name
    self.age=age
    
    def info(self):
       print("I am",self.name,"I am ",self.age,"years old")
    def make_sound(self):
     print("meow")

class dog:
     def __init__(self,name,age):
      self.name=name
      self.age=age

     def info(self):
      print("Iam",self.name,"I am ",self.age,"years old")

     def make_sound(self):
      print("bark")

object1=cat("Micky",2)
object2=dog("Wolfie",9)
object1.info()
object2.info()