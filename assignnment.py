# -*- coding: utf-8 -*-
"""Assignnment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1imVDfJhNaQG98Z42JRnp5RFbwjgMnBv3

Display Message in Python
"""

#This is single comment
'''multiline 
comment'''
print("Hello all")

"""Input in Python"""

name=input("Enter your name:")
print(name)

"""Data Type In Python

1. Number
"""

n1=234
n2=214
print(n1)
print(n2)
print(n1+n2)
n3=432.90
print(type(n3))

"""2. String"""

str="Welcome to python"
print(str)
print(str[1:4])
print(str[-2])
print(str*2)
print(str+' language')
print(str.upper())
print(str.lower())
print(str.replace('to','programming'))

"""3. List"""

list1=[10,20,30,40,50]
list2=["Akshata","Pinki","Shravani","Rutuja","Riya"]
list3=[101,"Akshata",102,"Riya",103,"Rutuja"]
print("List elements are:")
i=0
while i<list2.__len__():
  print("At index",i,"element is",list2[i])
  i=i+1

#list operations
#slice
print(list2[0:3])
print(list1[-4:-1])

#append
list1.append(60)
print("after append:",list1)

#insert
list2.insert(2,"aditi")
print("after insert:",list2)

#extend
list2.extend(list3)
print("after extend:",list2)

#update
list3[1]=100
print("updated list:",list3)

#delete
del list1[2]
list2.remove("Akshata")
print("after delete:",list1,"after remove:",list2)

"""4. Tuples"""

tuple1=(10,20,30,40)
tuple2=("ak","pk","ck","dk","mk")
print(tuple1[2])
print(type(tuple2))
print(tuple1[-4:-1])
for element in tuple2:
 print(element)
a=tuple1.__len__()
print("length of tuple1:",a)
tuple3=tuple1+tuple2
print(tuple3)
del tuple3
#we cannot add or delete particular element because tuples are immutable

"""5. Set"""

set1={10,20,30,40,50}
set2={100,13.24,"hello",(1,2,3,4)}
set3={1,2,3,4,5}
set4={6,4,3,5,7}
print(set2)

#set operations
set1.discard(20)
print("after discard:",set1)

set2.remove("hello")
print("after remove:,set2")

set1.pop()
print("after pop:",set1)

set5=set3|set4
print("after union:",set5)

set6=set3.intersection(set4)
print("after inmtersection:",set6)

set7=set3-set4
print("after set difference:",set7)

set8=set3^set4
print("after symmetric difference:",set8)

"""6. Dictionary"""

dict1={1:"ak",2:"pk",3:"dk",5:"sk"}
print(dict1[2])
for i in dict1:
  print("elements in dict1 at key:",i,"value:",dict1[i])

#dictonary operations
print("print all keys:",dict1.keys())
print("print all values:",dict1.values())

dict1[1]="bk"
print("after update:",dict1)

del dict1[5]
print("after delete:",dict1)

dict1.pop(1)
print("after pop:",dict1)

print("get value of key 2:",dict1.get(2))

dict1.clear()
print("after clear:",dict1)