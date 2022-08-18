'''
传递字典
函数中传递字典。在 Python 中，使用**作为形参接受实参传递的键值对。注意区别：
在形参列表中，*表示传递空元组、**表示传递字典。
'''

def employee(first_name, last_name, **employee_infor):
    '''
    创建字典，存储所有员工信息
    :param first_name:
    :param last_name:
    :param employee_infor:
    :return:
    '''
    employee = {}
    employee['first_name'] = first_name
    employee['last_name'] = last_name
    # 使用for循环存储所有的其他的键值对信息
    for key, value in employee_infor.items():
        employee[key]= value #注意key不用引号，否则只能显示组后一个实参

    return employee

my_employee = employee('Yoni', 'ma', location='Beijin', dep='Big data')
print('print my employee information:\n')
for key, value in my_employee.items():
    print(key+":"+value+"\n")

    