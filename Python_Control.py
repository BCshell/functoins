'''
控制结构就是控制程序执行顺序的结构，PYTHON有三大控制结构，分别是顺序结构，
分支机构以及循环结构。任何一个项目或者算法都可以使用这三种结构来设计完成。
这三种控制结构也是结构化程序设计的核心，与之相对的是面向对象程序设计。

有名的 c 语言就是结构化语言，没有对象
而 c++、Java 或者 python 等 都是面向对象的语言

'''

'''
顺序结构：就是按照代码的顺序执行，也就是一条一条语句顺序执行。
代码块又称为语句块，是一组代码的集合。在 Python 语言中，python 根据缩进来
判断代码行与前一行的关系。如果代码的缩进相同，python 认为它们为一个语句块；否
则就是两个语句块。一般使用 tab 按键缩进代码，有的 IDE 自动缩进代码 ，比如
pycharm。 
'''

'''
分支机构又称为选择结构，意思是程序代码根据判断条件，选择执行特定的代码，如果条件为真，程序程序一部分代码
否则执行另外一部分。 

在 Python 语言中，选择结构的语法使用关键字 if、elif、else 来表示，具体语法如下：
语法 1：if 语句，判断条件为真，执行语句组
if 判断条件：
语句组
1. 判断条件就是前面的各种运算符表达式的一种，或者几种的组合，比如 age >= 18;
2. 判断条件后面是以冒号（:）结尾；
3. 如判断条件为真，执行语句组（一行或多行代码）；
4. 语句组为一个代码块，使用缩进表示

'''
merried = True
if merried:
    print("请接受我们的夫妇套餐,并且享受打 8折优惠")
    print("还请帮忙宣传我们餐馆，多谢！\n")
'''
语法 2: 
if-else 语句，判断条件为真，执行语句组 1；否则执行语句组 2
if 判断条件：
    语句组 1
else:
    语句组 2

'''
#if-else 语句
merried= False
if merried:
    print("请接受我们的夫妇套餐,并且享受打 8折优惠")
    print("还请帮忙宣传我们餐馆，多谢！\n")
else:
    print("请接受我们的单身套餐，并且享受 9折优惠")
    print("也请帮忙宣传我们餐馆，多谢！\n")

'''
语法 3: 
if-elif-else,有三个判断条件的情况，只有符合其中的一个，才执行相应的代码,然后跳出
所有判断语句。
if 判断条件 1：
    语句组 1
elif 判断条件 2：
    语句组 2
else:
    语句组 3

'''
#if-elif-else 语句
merried= False
double= True
if merried and double:
    print("请接受我们的夫妇套餐,并且享受打 8折优惠")
    print("还请帮忙宣传我们餐馆，多谢！\n")
elif merried or double:
    print(" 请接受我们的情侣套餐，并享受 7.5折")
    print("还请帮忙宣传我们餐馆，多谢！\n")
else:
    print("请接受我们的单身套餐，并且享受 9折优惠")
    print("也请帮忙宣传我们餐馆，多谢！\n")

'''
语法 4: 
if-elif-elif-.....-else,有多个判断条件的情况，只有符合其中的一个，才执行相应的代码
if 判断条件 1：
    语句组 1
elif 判断条件 2：
    语句组 2
elif 判断条件 3:
    语句组 3
else:
    语句组 4
'''
#if-elif-elif-else 语句
merried= False
double= False
break_up= True

if merried:
    print("请接受我们的夫妇套餐,并且享受打 8折优惠")
    print("还请帮忙宣传我们餐馆，多谢！\n")
elif double:
    print(" 请接受我们的情侣套餐,并且享受 7.5折优惠")
    print("还请帮忙宣传我们餐馆，多谢！\n")
elif break_up:
    print("请接受我们的安慰套餐，并且享受 7折优惠\n")
else:
    print("请接受我们的单身套餐，并且享受 9折优惠")
    print("也请帮忙宣传我们餐馆，多谢！\n")

'''
语法 5： 
嵌套代码块，if语句里面嵌套使用 if语句，嵌套的if语句是上面 4种语法的任何一种。
if 判断条件 1：
    if 判断条件 2:
        语句组 1
    else：
        语句组 2
else:
    语句组 3

'''
#嵌套语句
merried= False
double= False
break_up= True
if not merried:

    if double:
        print(" 请接受我们的情侣套餐,并且享受 7.5折优惠")
        print("还请帮忙宣传我们餐馆，多谢！\n")

    elif break_up:
        print("请接受我们的安慰套餐，并且享受 7折优惠\n")

    else:
        print("请接受我们的单身套餐，并且享受 9折优惠")
        print("也请帮忙宣传我们餐馆，多谢！\n")
else:
    print("请接受我们的夫妇套餐,并且享受打 8折优惠")
    print("还请帮忙宣传我们餐馆，多谢！\n")

# 循环结构
'''
不断的重复为循环。循环结构是在一定条件下反复执行某部分代码的操作，是
python 程序数据中使用率最高的一个结构。在 Python 语言中，常见的循环结构有 
for循环和 while 循环。
'''

'''
for 循环为循环结构的一种。在 Python 中，for 循环是一种迭代循环，也就是重复
相同的操作，每次操作都是机遇上一次的结果而进行。for 循环经常用与便利字符串、列
表、字典等数据结构。具体语法为：
for 变量名 in 序列:
    语句组
    
5. for 循环也被称为 for--- in 结构。变量名为序列中的一个元素，遍历完所有元素循环结束。
在每一次的循环中，执行语句组。
6. 以冒号（结尾）
7. 语句组为一个语句块，具有相同的缩进。
8. 易错点：很多同学忘记缩进，得到了不同的结果。
for 循环-缺点：
9. 程序开始时必须提供输入数字总数。
10. 大规模数字求平均值需要用户先数清楚个数。
11. for 循环需要提供固定循环次数

'''
# 遍历字符串
str_data = 'Now is better than never'
count = 0
for str_d in str_data:
    print('遍历字符串：',str_d)
    if str_d == 'e':
        count+=1
    print(f'在字符串{str_data}中，字母n出现的次数是{count}\n')

'''
遍历整个列表
遍历整个列表是利用 for 循环得到列表中的每一个元素值，然后执行相同的操作。但
同时需要用到 index 和 value 值的时候，python 利用 enumerate()函数。 函数
enumerate()的参数为可遍历的变量，如字符串，列表等均可，返回 enumerate 类。
'''
name_fuyao=['扶摇','周叔','国公','无级太子','医圣','非烟殿主','穹苍']
print(f"列表元素有：{name_fuyao}")
#对列表中每一个元素执行相同的操作
for name in name_fuyao:
    print(name.title()+ ' 是扶摇电视剧中的角色名字。')

#练习题：循环外执行，如果缩进以后变成什么结果呢？
print("\n你感觉电视剧《扶摇》好看吗？")

# 使用enumerate()函数得到索引和值
for index ,name in enumerate(name_fuyao):
    print(name.title()+f' 是扶摇电视剧列表中第 {index} 角色名字。')

'''
for循环的另外一种常见用法是创建数值列表，在项目中经常用到，因为列表非常适合
用于存储数字集合。如果需要生成数字序列，可以使用内置 range()函数与 list()函数结合
生成，也就是 list(range())。
list函数把 range()函数生成的数字转化为数值列表。range()函数几
乎能够创建任何需要的数字集；如果需要获取列表的长度，则 len 函数可以达到目的。

语法：
range(start,end,step=1): 
注意：顾头不顾尾，生成的列表是从 start开始，到 end-1为止。

例子：
range(10):默认 step＝1，start＝0,生成可迭代对象，包含[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(1,10):指定 start＝1，end＝10，默认 step＝1，生成可迭代对象，包含[1, 2, 3, 4, 5, 6, 7, 8, 9]
range(1,10,2):指定 start＝1，end＝10，step＝2，生成可迭代对象，包含[1, 3, 5, 7, 9]
'''
#生成数字序列
for i in range(1,11,2):
    print(F"10以内的奇数是 {i}")

#len()求列表的长度，当列表不知道长度的时候，使用
a=[1,2,3,4]
for i in range(len(a)):
    print("当列表很长，使用 len()函数获的长度，用for访问列表元素的值",a[i])

#list()+range()=数值列表
even_numbers=list(range(2,11,2))
for i in even_numbers:
    print(f"10以内的偶数是{i}")
'''
for循环的另外一个常用用法是列表解析。列表解析是将 for循环和创建新元素的代码合
并成一行。在项目中，这个知识点经常被使用。
'''
squares=[value**2 for value in range(1,11)]
print('10以内的平方数生成一个列表',squares)

# 非列表解析
squares=[]
for value in range(1,11):
    squares.append(value**2)
print('10以内的平方数生成一个列表',squares)

# 遍历字典 dictionary
'''
字典中的键值对可能有上百万个。Python 支持使用 for 循环遍历字典，包括遍历所
有键值对（使用 items()方法）、遍历字典中的所有键（使用 keys()方法）以及遍历字典
中的所有值(使用 values()方法)。

'''
# 构建一个字典，记录各宫嫔妃的年薪银子，单位是两
name_dictionary={'妃子':300,
'皇后':1000,
'皇贵妃':800,
'贵妃':600,
'斌':200}

print(' ')
#使用 for()循环遍历字典中的 key-value,方法 items()返回键值对列表
print("各个级别的嫔妃的年薪是:")
for key,value in name_dictionary.items():
    print(f'\t{key} 的年薪是 {value} 两')

print(' ')
#遍历字典中的所有键，使用方法 keys()
print('后宫嫔妃的级别有:')
for name in name_dictionary.keys():
    print(f'\t {name}')

# 遍历字典中的所有值，使用的方法是 values()
print('后宫嫔妃的年薪有以下结构组成：')
for value in name_dictionary.values():
    print(f'\t{value}')

# 嵌套 for 循环
# for i in range(0,4):
#     for j in range(0,7):
#         print("*",end="")
#     print(' ')
#
# for i in range(1,8,2):
#     for j in range(i):
#         print("*",end="")
#     print(' ')

# 项目一 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}*{i} = {i*j}', end=' ') # 不换行，用end
#     print('')

# 项目二 打印图

# for i in range(1, 8, 2):
#     for j in range(i):
#          print('*', end='')
#     print(' ')

# for i in range(1, 8, 2):
#     for j in range(i):
#         print('*', end=' ')
#     print(' ')
#
# for i in range(5, 0, -2):
#     for j in range(i):
#         print('*', end=' ')
#     print(' ')



