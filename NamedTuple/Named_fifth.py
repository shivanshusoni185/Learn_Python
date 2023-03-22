from collections import namedtuple
#Define two named tuple
Person=namedtuple('Person',['name','age','gender'])
Address=namedtuple('Address',['street','city','state'])
#create instance of the named tuple
person=Person('shivanshu','25','male')
address=Address('medanta road','indore','Mp')

#Merger the named tuples
Contanct=namedtuple('Contact',Person._fields +Address._fields)
contact=Contanct(*person,*address)

#Access the fields to be merged
print(contact.name)
print(contact.age)
print(contact.city)
print(contact.state)