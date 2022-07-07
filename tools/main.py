# main：自己模拟的入口文件
# Python标准库提供了keyword模块，输出当前版本的所有关键字
import keyword

keyword.kwlist
print(keyword.kwlist)

# hello world
name = 'Hello World!'
print(name)

# 条件语句，python最具特色的就是使用缩进来表示代码块
bNew = True
if bNew:
    print('new')
else:
    print('old')

# python字符串：string，Python 中的字符串不能改变
# python中6个标准的数据类型：
# 数字（Number），不可变，python有4中数字类型：整数（int）、布尔类型（bool）、浮点数（float）、复数（complex）
# 字符串（String），不可变
# 元组（Tuple），不可变
tuple = (1, 2, 3)
# 列表（List），可变
lists = list()
lists2 = []
# 集合（Set），可变
sites = {'Google', 'Taobao', 'Baidu', 'QQ'}
print(sites)
a = set('1231')
b = set('23424')
print(a)
# 字典（Directory），可变
dict = {}
dict['one'] = 'one'
dict[2] = 2
tiny_dict = {'1': '1', 2: '2'}
print(dict['one'])
print(dict[2])
print(tiny_dict)
print(tiny_dict.keys())
# type()和instance()
