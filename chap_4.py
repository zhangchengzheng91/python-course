# 4-1 一个简单的数据库
# 一个将人名用作健的字典。每个人都用一个字典表示
# 字典包含健'phone'和'addr'，它们分别与电话号码和地址相关联
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}
# 电话号码和地址的描述性标签，供打印输出时使用
labels = {
    'phone': 'phone number',
    'addr': 'address'
}

# name = input('Name: ')
#
# # 要查找电话号码还是地址？
# request = input('Phone number (p) or address (a)?')
#
# # 使用正确的键
# if request == 'p': key = 'phone'
# if request == 'a': key = 'addr'
#
# # 仅当名字时字典包含的键时才打印信息
# if name in people: print("{}'s {} is {}".format(name, labels[key], people[name][key]))

# 4-2 字典方法示例
# 一个使用 get（）的简单数据库
# 在这里插入代码清单4-1中的数据库字典（字典people）
name = input("Name: ")
# 要查找电话号码还是地址
request = input('Phone number (p) or address (a)?')

# 使用正确的键
key = request
if request == 'p': key = 'phone'
if request == 'a': key == 'addr'

# 使用get 提供默认值
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

print("{}'s {} is {}.".format(name, label, result))