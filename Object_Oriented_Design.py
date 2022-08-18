# 程序设计方法
'''

常用的程序设计方法：结构化程序设计 与 面向对象程序设计。
结构化程序设计：
结构化程序设计方法的主要思想'自上而下，逐步求精'
主张按功能来分析系统需求。需求逐步细化为一个个小的功能，所有功能的组合为一个大的系统，因此它又叫做
面向功能的程序设计方法。每一个功能对应一个函数，函数是结构化程序设计中最小的程序单元。
整个过程由一个一个函数组成，而整个程序的入口是一个主函数(main())，由主函数调用其他函数，函数之间的依赖来构成
整个程序的功能。
结构化程序设计非常强调某个功能的算法，算法由一系列操作组成。任何简单或复杂的算法都可以由顺序结构，
选择结构，循环结构这三种基本结构来构成。

面向对象程序设计：
面向对象设计(object Oriented Programming, oop）是从自然界来的，在系统构造中，
尽可能的利益人类的自然思维模式，强调以现实世界中的事物（对象）为中心来思考，认识问题，
并根据这些事物的本质特征，把它们抽象表示为系统中的类。然后由类创建对象。这使得软件系统的
组件可以直接的映像到客观世界，并保持客观世界中事物及其相互关系的本来面貌。这个是面向对象的特点，
一切皆对象。

面向对象方法的三个特征：
    封装性：将面向对象实现细节隐藏起来，通过一些公共的接口方法来供外部调用对象的功能。
    继承性：是面向对象实现的的重要手段,子类继承父类, 子类直接获得父类的非private 属性和方法
    多态性：子类对象可以赋值给父类对象引用, 但运行的时候仍然表现出子类的行为特征,
同一个类型的对象在执行同一个方法时, 可能表现出不同的特征
'''

'''
面向对象概念：
面向对象中的第一个概念就是类，class，类的意思有两个。
第一个是种类；许多相似或相同事物的综合：类型|分类|类别|分门别类。具有共同
特征的事物所形成的种类，例如树木有好多种类型，杨树、柳树、松树、柏树等；
第二个是相似；相像：类同|类似 致相像。
例句：这几道数学题的题型类似，解法也大体相同。在 Python 变成语言中，类也是一些相似事物的综合。比如人，人具有 2 个胳膊，2
条腿等特征；并且人会走路，说话等行为。
在 Python 语言 中，这些描述事物的特征称为属性，而表示事物的行为称为方法（也就是函数，在面向对象里面一切行为都是方法，没
有函数），把两者合并一起就是 python 语言的类。
类 Class 就是用来描述具有相同属性和方法的事物集合。也就是类具有相同的属性和方法。

另外一个重要的概念是对象(Instance),
在 Python 语言中，对象就是类的一个具体事物 ，
比如人是一个类 ，那么刘德华就是一个具体的事物，就是人的一个对象。刘
德华就具备人的属性，2 个胳膊，两条腿以及会走路，会说话等行为.

类和对象都是名词。两者的区别是：每一个对象自动具备类中的属性和方法，但是具
体的数据可能不同，比如刘德华的胳膊可能比杨幂的长一点等；而类是一个模版，可以创
建多个对象，个数没有限制，比如类  人，可以创建很多个对象。根据类创建对象，这个过
程称为实例化。实例化以后对象就具备了对象的属性和功能（方法）。

'''
# 如何定义类
# class ClassName():
#     '''类定义'''
#     def __int__(self,var1,var2):
#         # 类属性
#         self.var1 = var1
#         self.var2 = var2
#         self.var3 = 0
#     def function1(self,var3):
#         #方法
#         print(self.var1 + var3)
#     def function2(self):
#         #方法
#         print(self.var2)
# class 表示类的定义，为 python 的关键字。关键字是预先保留的标识符，每一个关键字有特殊的意思。
# 如何判断一个单词是不是关键字，使用 keyword 模块，如何是则返回 True
# import keyword
# print ("class 是不是关键字", keyword.iskeyword('class'))

'''
ClassName 为类的名字，需要与关键字 class 中间空一格。类名必须是首字母大写，
定义中的()是空的表示从空白创建这个类。

""""类定义 """ 为类的注释说明，表面这个类的功能

方法__init__()

关键字 def 开始的表示函数，但是在类里面称为方法。方法与函数的调用方法不同。
函数直接使用，方法必须使用(.)调用。 

注意：所有 def 开头的方法必须空一个 tab 键才表示类的代码块，否则不是类里面
的一部分。

__init__方法是类中的特殊方法，init 前后都有两个下划线（记住是两个下划线，不是
一个，并且不是中文状态下的）

该方法的作用是用来创建类的属性，比如人的姓名，出生地，两个胳膊，两条腿等。

形参列表 self、var1、var2 中，self 是必须要有的，并且放在最前面。当类实例化
对象的时，自动传入实参 self，它的作用是让对象能访问类中的属性和方法，本质上
它是一个指向对象本身的引用。类里面的其他方法也必须有一个 self 参数，才可以访
问类里面的属性。

self.var1 self.var2 self.var3 定义的变量表示该类的属性，是可以被类中的所有方
法访问，也可以被实例化的对象访问。此类有三个属性，var1,var2 以及 var3，其中
var1 与 var2 需要实例化对象的时候传入参数，var3 是采用默认的值，当然也可以
被修改。

方法 function1 与 function2 表示类中的两个方法，也就是该类所具有的行为，可
以被对象访问。这些方法也必须有一个 self 参数，才可以访问类里面的属性。方法的
名字最好是具有描述意义的单词，比如 describe_user()，看到名字就会知道该方法
的功能. 
'''

'''
example:
定义一个 People 类，具有 4 个属性：姓名、地址、职业以及默认属性年龄
（默认值 18 岁）和一个方法自我介绍。四个属性放在__init__方法里面，创建一个新
的方法命名为 introduce_you 表示自我介绍，具体代码如下
'''


class People():

    def __init__(self, name, address, career):
        self.name = name
        self.address = address
        self.career = career
        self.age = 18  # 默认的属性值，不需要在 init 方法列表体现

    def introduce_you(self):
        # format()方法的另外一个用法，构造消息。也可以把消息写在一个函数里面
        introduce = 'Python, 我是{n},今年{a},来自{l},我的工作是{c},nice to meet you guys'
        mess = introduce.format(n=self.name,
                                l=self.address,
                                a=self.age,
                                c=self.career)
        print(mess)
        # 在 People 类中添加两个方法：read_age 用来获取人的年龄；update_age 用来更
        # 新年龄，具体如下：
    def read_age(self):

        # 读取年龄属性
        print('{}今年{}岁'.format(self.name, self.age))

    def update_age(self, new_age):
        # 更新属性的方法
        if new_age < 0:
            print('年龄不能为负数')
        else:
            self.age = new_age

# 创建对象
'''
根据类模版创建对象，也称为实例化。实例化可以任意多个， 没有限制。
语法：
对象名 = 类名(属性参数列表)
对象名就是变量名，命名规则与变量相同，但是必须小写，因为首字母大写的表示类

属性参数列表就是类方法__init__里面的，其中 self 自动传递，不需要指定

对象创建成功以后就可以访问类中属性和方法，使用的是句点（.）表示法：
语法：
对象名.属性
对象名.方法名字

'''
print('实例化对象 little_ma')
little_ma = People('Ray', 'Beijing', 'software engineer')
print('对象调用属性采用逗点表示法.')
print(f'python guys, I am {little_ma.name}, I come from {little_ma.address}, my job is {little_ma.career}, nice to meet you guys')
print('')
print('对象调用方法，也是采用逗号表示法')
little_ma.introduce_you()

print('\n 实例化另外一个对象 kim')
kim = People('Kim', '上海', '数据分析师')
kim.introduce_you()

# 修改属性的值
'''
实例化对象以后，其属性值是可以别修改的。有两种方法修改：

第一种是对通过实例(对象)直接修改，语法是：对象.属性=新的值；
第二种是在类中写方法进行修改想要修改的属性。

'''

'''
修改小马哥的年龄从 18 岁到 33 岁，然后修改职业变成数据分析师。最后在试
着修改小马哥的年龄为-1 岁，程序提示年龄不能为负
两种方法修改属性的值：
1。通过对象（实例）修改
2。通过方法设置
'''
# 通过对象修改
little_ma.age = 31
little_ma.read_age()
little_ma.career='数据分析师'
print('{} 的新职业是{}'.format(little_ma.name, little_ma.career))

# 通过方法修改
little_ma.update_age(33)
little_ma.read_age()
little_ma.update_age(-1)
little_ma.read_age()

# 继承
'''
在 Python
语言中，继承是一个类继承另一个类的所有物品，也就是属性和方法，其中继承的类被称
为父类；被继承的子类。子类继承了父类中的所有方法和方法，同时还可以有自己的属性
和方法，就好比儿子继承了父亲的事业，但是儿子自己也有自己的事业


'''

class Father:
    '''父类继承'''
    def __init__(self, var1, var2):
        '''定义父类属性'''
        self.var1 = var1
        self.var2 = var2
    def function1(self):
        '''父类方法'''
        print(f'{self.var1}')

class Child(Father):
    '''子类的定义'''
    def __int__(self, var1, var2):
        ''' 定义子类属性（父类的 +子类的）'''
        super().__init__(var1,var2) #父类的属性
        self.var3 =1 # 子类的属性
    def function1(self):
        '''子类的方法，可以重写父类的方法'''
        print(f'{self.var3}')

    def function2(self,var4):
        '''定义子类自己的方法'''
        self.var3 = var4
        print('New var3 is', self.var3)
'''
定义父类 Father,具有属性 var1 和 var2，并且有方法 funtion1。父类必须在子类的
前面，并且在一个文件中.

定义子类 Child：

开始也是用关键字 class 表示，Child 是子类的名字，首字母必须大写

括号中必须指定父类的名字，以冒号结尾

三个 def 组成的类代码块必须缩进，否则不是子类的一部分。你可以定义多个方法，
没有限制

第一个方法 是定义子类的属性，包括了父类的属性和自己的属性

父类的属性使用特殊的函数 super()，将父类与子类关联起来。super 函数调用父类
的__init__方法，让子类包含父类的属性。

子类还可以定义自己的属性，通过 self.var3 定义，var3 可以是任意的变量名字，但
是必须符合变量命名规则。

第二个方法function1 是和父类一样的方法，称为重写父类的方法。因为父类的方法不能满足
子类的要求时，子类可以重新写父类的方法

第三个方法function2 是子类独特的方法
'''

'''
example:
定义会员类 Member，继承类父类 People.

"""
定义会员类，继承类父类 People
会员类，有自己的属性 introduction
"""

'''

class Member(People):
    """会员类，继承人类"""
    def __init__(self,name, address, career, hope):
        super().__init__(name, address, career)
        self.hope = hope
    def introduce_you(self):
        """ 重写父类的方法"""
        introduce = ' Python 实战圈的圈友们好，我是{n},今年{a},来自{l}.我的工作是{c},很高兴认识大家！在咱们圈子里，我希望自己能 {h}.'
        mess = introduce.format(n=self.name,
                                l=self.address,
                                a=self.age,
                                c=self.career,
                                h=self.hope)
        print(mess)

    def set_hope(self, hope):
        """定义子类的方法"""
        self.hope = hope
        print("{}的希望是{}".format(self.name, self.hope))

Grace = Member("Grace","上海",'数据分析师','彻底学会 Python')
Grace.update_age(19)  # 调用父类的方法
Grace.introduce_you()  # 调用自己重写的方法

# 导入类
'''
在 Python 中，类可以被存放在模块中，然后在主程序中直接调用。也就
是通过 import 类名 或者 from 模块名字 import 类名。

例子：把父类 People 和 子类 Member 单独放在文件 people.py 中，然
后通过 from 的形式调用。还是上面的例子，圈友 Grace 的自我介绍放在主函
数中，以一个单独的文件使用。运行结果与上面一致。

此方法的主要目的是为了简化主程序的逻辑，不需要考虑类的定义，使得我们的注意力能专心在主
程序的逻辑而不是定义类

'''


