# import employee_model
# my_employee = employee_model.employee('Yoni', 'Ma', location = 'Beijing', dep = 'Big Data')
# print('Print my employee information: \n')
#
# for key, value in my_employee.items():
#     print(key+ ":" +value+ "\n")

# 4种方法把模块中函数导入到主体文件中
# 导入整个模块文件的函数，必须使用module_name.functoin_name()调用
# import employee_model
# my_employee = employee_model.employee('Yoni', 'Ma', location = 'Beijing', dep = 'Big Data')

#导入模块中特定的函数，调用时候不用模块的名字
# from employee_model import employee
# my_employee = employee('Yoni', 'Ma', location = 'Beijing', dep = 'Big Data')

# 使用as 制定函数的别名
# from employee_model import employee as em
# my_employee = em('Yoni', 'Ma', location = 'Beijing', dep = 'Big Data')

# 使用*导入模块中所有函数，但是加载会很慢,耗时
from employee_model import *
my_employee = employee('Yoni', 'Ma', location = 'Beijing', dep = 'Big Data')
