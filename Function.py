def welcome_python(member_name, hope):
    print(f'welcome to my world,{member_name}')
    print(f'\t{hope}')

welcome_python('KIM','wish you can keep on')
welcome_python('Grave','wish you can find your ideas')
'''
位置参数
位置实参是基于参数的位置，实参与形参的顺序必须相同。每一个实参都关联到函数
定义中的一个形参。比如上面的例子。如何位置顺序不对，则结果可能大不一样。位置实
参的位置很重要。如果实参的位置和形参的相反，虽然代码可以运行，但是意思肯定错误
了。也就是语法正确，语义有问题。该传递方式也是最常用的方式。

关键字参数

关键字实参
每一个实参都有变量名+值组成，并且不用考虑函数形参的顺序。调用形式：形参名
字=“值”。
优点：无需考虑实参的顺序，易错点：形参的名字一定要正确

默认值
如果形参的值，固定不变，则可以在指定默认值。比如希望每一个加入 Python 实战圈
的人都可以坚持下去，则形参 hope 指定为默认值即可
'''
print('颠倒实参顺序,结果完全不同 ')
welcome_python('希望你能坚持下去。','Kim')
welcome_python('希望你可以找到想要的。','Grace')

# 关键字实参
welcome_python(hope= '希望你能坚持下去。',member_name='Kim')
welcome_python(member_name='Grace',hope='希望你可以找到想要的。')

# def welcome_python(member_name,hope='希望你能坚持下去'):
# # 定义带有默认值参数的函数
#     print(f'你好，{member_name} ,欢迎加入 Python 实战圈')
#     print(f'\t{hope}')

'''任意数量的实参
有时候，我们不知道需要传递多少个实参。函数调用时候，无需考虑形参的个数。可
以任意指定实参的数量。PYTHON 通过使用*，让程序创建一个空元组，可以接受任
意数量的参数值。'''
# 例子：
def welcome_python(*member_names, hope='希望你能坚持下去'):
# 任意多个参数的函数
    for member_name in member_names:
        print(f'你好，{member_name}. 欢迎加入 Python 实战圈')
        print(f'\t{hope}')
welcome_python('Kim','Grace','Nelson Lam','None')

'''
返回值return  
函数运行完成以后，如果需要返回一个值给调用该函数的地方，则使用 return 返回。
函数返回值的类型可以是基本数据类型，也可以是字典、列表等。

返回值能让主程序简单，把大部分处理工作交给函数。比如 加入 Python 实战圈的人
有外国人，名字分为 last name 与 first name. 则欢迎加入 python 实战圈的语句中，名
字的处理可以使用函数解决。
'''

def full_name (first_name,last_name):
# 带有返回值的函数
    person = first_name + ' ' + last_name
    return person.title()

name = full_name('Nelson', 'lam')
welcome_python(name)

# 传递数据结构
# 列表也可以作为函数的参数，函数就可以直接访问列表中的元素
def welcome_python(member_names, hope = 'hope you can keep on'):
    for member_name in member_names:
        print(f'hello, {member_name},welcome to python world')
        print(f'\t{hope}')
    list_name = ['Kime','Grace','Nelson','None']
    welcome_python(list_name)

# 传递字典
'''
函数中传递字典，在Python中，使用**作为形参接受实参传递的键值对。
注意区别：在形参表中，*表示传递空元组， ** 表示传递字典

'''

#盒子的秘密
'''
函数可以被看做一个盒子，分为盒子外和盒子内，盒子内就是函数的内容，也被称为私有的
内部的资源只能被自己使用。
 
盒子外就是函数之前的内容，也称为是外部内容，函数不能直接使用，，只能通过函数传递的方法进行。
盒子内与外的变量名字可以相同或者不同，不冲突。

函数的return可以看作是和外部沟通的桥梁.

盒子内部的变量是局部变量，也就是定义在函数内部的变量并且作用域为整个函数；
盒子外的变量为全局变量，作用域为整个文件。 

'''
# 这个是全局变量
add_sum = 3
def sum_add(para, para2):
    add_sum = para + para2
    print('函数内部变量add_sum= ', add_sum)

    return add_sum
# 调用sum函数
ad_sum = sum_add(18,31)
print('18+31=', ad_sum)

print('函数外部是全局变量:add_sum= ', add_sum)

# 将函数存储在模块中
'''
有时候，我们可以将函数存在单独的文件中，隐藏其逻辑。这样就可以把主要精力用
在主体程序。
比如把员工信息的函数存放在文件 employee_model.py 中，则主函数直接调用该
文件即可。

'''






