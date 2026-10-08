class emni:
    def __init__(me, name , age=18 ):
        me.name = name 
        me.age = age 
p1= emni("asif")
p2 =emni("jhboids", 27 )

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p1.__dict__)  
print(p2.__dict__)  

def bark(self):
    print(self.name + " woof woof")


bark(p1)
bark(p2)