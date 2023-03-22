from collections import namedtuple

Participant=namedtuple("Partcipant",["Name","Age",'Country'])
p1=Participant('shivanshu','23','india')
p2=Participant('Sahil','21','USA')

#Accessing element in the differnet way in namedTuple
#Access through index
print(p1[0]+ p1[2])
print(p2[0]+p2[1])

#Access through name
print(p1.Name+p1.Age)
print(p2.Name + p2.Age)

#Acess through getAtrribute
print(getattr(p1,'Name'))
print(getattr(p1,'Age'))

#Transform list and tuple to namedtuple

l1=['shivam','27','JBP']
p3=Participant._make(l1)
print(p3)

l2={'Name':'Nishi','Age':'19','Country':'Austraila'}
p4=Participant(**l2)
print(p4._asdict())

#replace is also available in named tuple
p4=p4._replace(Country='Germany')
print(p4._asdict())
print(p4._fields)
p4._replace(Name='Rajul')
print(p4._asdict())

#Default values are assigned with rightmost value
Student = namedtuple("Student", ["Name","Class","Age","Subject","Marks"], defaults = [10])
Student1 = Student("Arshia", 12, 17, "Maths")
print ( Student1 )