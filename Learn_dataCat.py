#vim: set fileencoding:utf-8
#coding=utf-8  #需要使用中文的地方需要加入调整编码。以上两种方式均可。
import numpy

print("hello world!")

int_num1 = 123
print(int_num1)

str_name = "彭曲波"
print(str_name)

list_myFamily = ["Apoul", "夏妈妈" , "彭爸爸" , '俺老婆']
print(list_myFamily)
print(type(list_myFamily))
print(list_myFamily[2])
for str_familyName in list_myFamily :
    print(str_familyName)

i = 0
while i < len(list_myFamily):
    if i == 0 :
        print("while 循环")
        print(list_myFamily[i])
    else:
        print(list_myFamily[i])
    i += 1

dic_family = {}
list_pqb= [34 , "男"]
dic_family["彭曲波"] = list_pqb
list_pbb= [60 , "男"]
dic_family["彭爸爸"] = list_pbb
list_xmm= [62 , "女"]
dic_family["夏妈妈"] = list_xmm
list_alp= [33 , "女"]
dic_family["俺老婆"] = list_alp

for name in dic_family:
    print(name)
    print(dic_family[name])
    print("------------")
print("彭曲波" in dic_family)
print("------------")
print(list_alp in dic_family.values())
print("------------")
print(dic_family.values().__len__())
# print(dic_family.values("彭曲波", ))
# print(help(dic_family.values()))
print("------------")

arr_family = numpy.array([["彭曲波" , "34" , "男"] , ["彭爸爸" , "60" , "男"] , [ "夏妈妈" , "62" , "女"] , [ "俺老婆" , "33" , "女"]])
print(arr_family[2,2])

print("34" in arr_family)


a = numpy.floor(10*numpy.random.random((3,4)))
print(a)
#print(a.ravel())
print("------------")
a.shape = (4,3)
print(a)
print("------------")
b = 10*numpy.random.random((3,4))
print(b)
print("------------")
c = (numpy.random.random((5,4))*1000)
print(c)
print("------------")


#部分数据类型是不能被修改的对象，例如：int、string，tuples、number等
a = 1
def fun(a):
    a=2

fun(a)
print(a)

#而部分数据类型的对象是可以被修改的，例如：list、dict等
b = []
def getList(c):
    c.append(1)
    c.append(2)
getList(b)
print(b)

class Person:
    name="aaa"

p1=Person()
p2=Person()
p1.name="bbb"
print(p1.name)  # bbb
print(p2.name)  # aaa
print(Person.name)  # aaa


class Person:
    name=[]

p1=Person()
p2=Person()
p1.name.append(1)
print(p1.name ) # [1]
print(p2.name ) # [1]
print(Person.name) # [1]

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
# Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

#is 判断对象是否同一个，==判断对象的值是否相同。首先要确定是什么类型？
a=0
b=0
print(a is b)
print(a == b)
print("a is",type(a),"      b is",type(b))

a=[0]
b=[0]
print(a is b)
print(a == b)
print("a is",type(a),"      b is",type(b))

a="0"
b="0"
print(a is b)
print(a == b)
print("a is",type(a),"      b is",type(b))
# print(help(int))

a=[0]
b=a.copy()
b[0]=1
print(a is b)
print(a == b)
print(a)
print(b)
print("a is",type(a),"      b is",type(b))
print(id(a),'=a',id(b),'=b')