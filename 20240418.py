# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
list1=list()

list2=list([1,4.5,'apple']) 

print(list1)
print(list2)

#%%
x=[]
y=[1,4.5,'apple']
print(x)

a1=y[1]    #串列是由0,1,2,..
a2=y[-1]   #負數是從後面開始
print(a1)
print(a2)

#%%
a=[2,3,4]
b=[2,7,3.5,'hello']
c=[]

d=[2,[a,b]]
e=a+b

x=a[1]
print(x)

y=b[1:3]   #取1到2,不包含位置3
print(y)

z=d[1][1][3] 
print(z)

b[0]=42   #取代0位置
print(b)

#%%
print(3*[1,2,3])


#%%
[1,2,3]==[3,2,1]
'C' in ['A','B','C']   #C是否串列裡
'D' not in ['A','B','C']


#%%
x1=[1,2,'B','A']

print('A' in [1,2,'B','A'])

print('A' not in x1)

print('C' not in [1,2,'B','A'])

#%%
list1 = [i for i in range(8)]  #產生一組元素放入串列
print(list1)

list2 =[i*2 for i in range(8)]  #放入串列前作處裡
print(list2)

#%%
C = [i for i in range(100)] 
F = [(i*8/5+32) for i in C]  #將串列做處理在放入串列
print(F)

#%%
L =[1,2,3,4,5,6]
del L[2]
print(L)

L =[1,2,3,4,5,6]
del L[2:4]
print(L)

#%%
print(len([1,2,5,8,9]))  #串列長度
print(max([1,2,5,8,9]))
print(min([1,2,5,8,9]))
print(sum([1,2,5,8,9]))

#%%
num=[3,4,5,6,1000,2000,100,1000]

print(num)

num.append(7)      #添加

print(num)

num.append(500)

print(num)

num[2]=1000        #修改

print(num)

num.remove(1000)   #只會刪除第一個1000

print(num)

del num[0]

print(num)

del1000_num = num.count(1000)   #count 計算串列內1000數量

while del1000_num >=1 :         #利用迴圈刪除
    num.remove(1000)
    del1000_num = del1000_num-1
print(num)    

#%%
a=[200,100,150,580,510,200,1110]
print(sorted(a))  #排序
print(a)          #但不會改變原始資料

a=[200,100,150,580,510,200,1110]
a.sort()          #排序會改變原始資料
print(a)

#%%
tuple1 =(1,2,3,4)
print(tuple1)

tuple2 = 1,2,3,4   #如沒有加()[]視為tuple
print(tuple2)

#%%
f =(2,3,4,5)
g =()
h =(2,[3,4],(10,11,12))

x =f[1]
print(x)
y =f[1:3]
print(y)
z =h[1][1]
print(z)

#%%
date=(6,True,'xyz')
num,bool,str = date   #依序投給前面的變數
print(num)
print(bool)
print(str)

#%%
a, *b=(1,2,3)
print(a)
print(b)

x,*y,z=(1,2,3,4,5)
print(x) #1
print(y) #[2, 3, 4] 串列
print(z) #5 

#%%
xyz=set()
xyz.add('A')
xyz.add(1)
xyz.add(False)
print(xyz) #{False, 1, 'A'} 不按順序

#%%
x ={3,3,3,6,6,6,7,7}
y ={6,6,3,3,7,7,7}
print(x == y)  #內容相等

print(x is y)  #不同集合 

print(id(x))   #查詢集合id

#%%
w1={1,2,3,4,5,1,2,3,4,5,5,4,3,2,1,234,567,1025}

print(len(w1))
print(max(w1))
print(min(w1))
print(20 not in w1)


#%%
#S={1,2,3,4,5}
#s={1,2,3,4,5}
# print(S+s)     #set無法使用
# print(S*s)
# print(S[1])
# print(S[1:3])

#%%
thisset = set(("Google", "lccnet", "yahoo","momo")) 

thisset.update({'apple',1000,'Microsoft',800}) #添加
print(thisset)

thisset.update([245,333],[512,625])  
print(thisset)

#%%
thisset = set(("Google", "lccnet", "yahoo","momo","yahoo"))
thisset.remove("yahoo")     
print(thisset)

#%%
thisset = set(("Google", "yahoo", "pchome", "Facebook"))
print(thisset)

x = thisset.pop()  #提取 從元集合移除
print(thisset)
print(x)

#%%
x ={"one":1,"two":2,"three":3}

a = x["two"]    
print(a)

x["two"] = 150  #更改
print(x)

x["four"] = 4  #如沒有key則新增
print(x)

#%%
x ={"one":1,"two":2,"three":3,"four":4}
print(x.pop("one"))
print(x.popitem())

#%%
x ={"one":1,"two":2,"three":3}
print(x.keys())
print(x.values())
print(x.items())



