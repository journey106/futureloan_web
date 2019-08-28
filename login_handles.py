
str1 = '12344555093aghjh dohhk**!'
print(str1.find('c'))
print(str1.index('a'))


mystr = ['a', 'b']
mystr.append('c')
print(mystr)
mystr = mystr+['d', 1, 'gk']+[3, 4]
print(mystr)
mystr.extend(['ou', 'qfhhhh', '007'])
print(mystr)

mystr.remove(1)
print(mystr)
mystr.pop(3)
print(mystr)
del mystr[3]
print(mystr)
mystr.clear()
print(mystr)
# del mystr
print(mystr)

mystr[0:5] = [1, 7, 6, 9]
print(mystr)
mystr.sort()
print(mystr)

print(len(mystr))
print(mystr*2)
mystr1 = (1, 2)
mystr2 = (3, 5, 7)
print(mystr.index(6))
# print(cmp(mystr1, mystr2))

mytuple = (1, 5)
a,b = mytuple
print(a, b)

a = [1,2,3,4,5,6,7,110,1,0,5]
a[2:5] = []
print(a[1:4:2])
print(a)
print(a[-1::-1])
print(a[::-1])
b = a.copy()
print(b)
print(a.count(6))

put = 'i like runoob'
putwords = put.split(" ")
putwords = putwords[::-1]
print(' '.join(putwords))


mydict = {1:2,"5":"a"}
mydict2 = {'a': 'ouou', 'c':"123"}
mydict.update(mydict2)
print(mydict)
mydict.pop("5")
print(mydict)
mydict.popitem()
print(mydict)
mydict.clear()
print(mydict2.items())

for i,k in mydict2.items():
    print(i,k)

print(dict([('Runoob', 1), ('Google', 2)]))
print({x:x**2 for x in(2,4,6)})
print(dict(Runoob=1, Google=2))

c = set()
print(c)
print(list(set([1,3,4,1,6,3,2])))

website = 'http://www.python.org'
python_index = website.find('python')
print(python_index)
print(website[python_index : python_index+len('python')])

best_language = "     PHP is the best programming language in the world!      "
best_language = best_language.strip().replace('PHP', 'Python')
print(best_language[::-1])

my_hobby = "Never stop learning!"
print(my_hobby[1:6])
print(my_hobby[1:])
print(my_hobby[:6])
print(my_hobby[:])
print(my_hobby[3::2])
print(my_hobby[2:-1])
print(my_hobby[-2:])
print(my_hobby[::-1])

age = 18
gender = 'male'
hobby = 'reading'
motto = 'never give up learin'

print('''**************************************************
个人信息展示
​
姓名（网名）
​
年龄：{}
性别：{}
爱好：{}
座右铭：{}
*************************************************'''.format(age, gender, hobby, motto))

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

vec = [2, 4, 6]
a =[[x, x**2] for x in vec]
print(a)

a = [3 * x for x in vec if x > 3]
print(a)

b = [3 * x for x in vec if x < 2]
print(b)

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
a = [x*y for x in vec1 for y in vec2]
print(a)
c = [vec1[i]*vec2[i] for i in range(len(vec1))]
print(c)

m = [str(round(355/113, i)) for i in range(1, 6)]
print(m)
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print([[row[i] for row in matrix] for i in range(4)])

print("----------------------")
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)

for i,v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
    print(i)

info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]

# info.remove('矮穷丑')
# info.pop(info.index('矮穷丑'))
# del info[3]
# info[3]=[]
print(info)

# flag = 1
# while (flag): print ('欢迎访问菜鸟教程!')

a, b = 0, 1
while b<1000:
    print(b, end=',')
    a, b = b, a+b

print('------')
max_num = 1
for i in [1,5,2,0]:
    if i>max_num:
        max_num=i
print(max_num)

for i in range(1, 10):
   # line = ' '
    for j in range(1, i+1):
       # line += "{} * {} = {}\t".format(j, i, j*i)
        print("%d * %d = %d" % (j, i, i*j), end='\t ')
   #print(line)
    print()

i = 1
while i < 10:
   j = 1
   while j <= i:
      print("{0} * {1} = {2}".format(j, i, i*j), end=" \t")
      j += 1
   i += 1
   print()

a = [1, 7, 4, 89, 34, 2]
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)

a = [1, 7, 4, 89, 34, 2]
# 选择排序
for i in range(len(a)):
    min_indx = i
    for j in range(i+1, len(a)):
        if a[j]<a[min_indx]:
            min_indx=j
    a[i], a[min_indx] = a[min_indx], a[i]
print(a)

print('-----------------------------------------------------------')
# 插入排序
a = [1, 7, 4, 89, 34, 2]
for i in range(1, len(a)):
    temp = a[i]
    j = i-1
    # 往前寻找，如果有比临时值的数 ，则后移，则将当前值作为临时变量存储，继续向前寻找
    while j >=0 and temp <a[j]:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = temp
print(a)

def print_num(start, end):
    num = []
    for i in range(start, end + 1):
       if (i %7 != 0) and (str(i).find("7") == -1):
           num.append(i)
    return num

print(print_num(1, 100))
print(sum([1,2,3]))

import os

print(os.getcwd())
print(os.path.abspath(__file__))


