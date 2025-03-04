# Class creation
class myClass:
    # private variable
   _privateVar = 27;
    # private method
   def _privMeth(self):
       print("I'm inside class myClass")
   def hello(self):
      print("Private Variable value:", myClass._privateVar)
    
foo = myClass()
foo.hello()
foo._privMeth