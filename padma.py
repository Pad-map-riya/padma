print("hello")
print("hello world")
list=[1,2,3,4,5]
for i in list:
    print(i)
    x=list[0]
    print(x)
    a=0
    while a<len(list):
        x=list[a]
        print(x)
        a+=1
dict1={'a':1,'b':2,'c':3}
for key,value in dict1.items():
    print(key,value)