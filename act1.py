class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("the dog's name is",self.name,"and the age is",self.age)
    def sound(self):
        print("dog sound is bark")

class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("the cat's name is",self.name,"and the age is",self.age)
    def sound(self):
        print("cat sound is meow")
dog1=dog("paul",4)
cat1=cat("tommy",7)

for i in(dog1,cat1):
    i.info()
    i.sound()
    
