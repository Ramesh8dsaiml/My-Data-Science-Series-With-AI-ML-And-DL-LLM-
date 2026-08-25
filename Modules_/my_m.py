# property :>>>>>  wee use @peroperty decorator on any methods in the class to use the method as a property .
class student:
     def __init__(self , phy, chme , math ):
          self.phy = phy
          self.chem = chme
          self.math = math
          self.percentage= str((self.phy + self.chem + self.math ) / 3 ) + "%"

     def calpercentage(self):
          self.percentage= str((self.phy + self.chem + self.math ) / 3 ) + "%"


stu1 = student(90, 80 ,95)
stu2 = student(80, 84 ,86)
stu3 = student(69, 79 ,93)
stu4 = student(59, 87 ,81)

print(stu1.percentage)

stu1.phy=  86
print(stu1.phy)
stu1.calpercentage() # 
print(stu1.percentage)
