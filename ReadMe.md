# Python

## 术语

- `模块：`尽量使用小写命名，decoder、html_parser 等
- `类名：`首字母大写，大驼峰
- `函数：`小写，下划线
- `变量名：`小写，下划线
- `常量：`大写，下划线
- `注释`：#后空格，段落使用空注释行

## Python 虚拟环境 virtualenv<https://github.com/walter201230/Python/blob/master/Article/advanced/%E4%BD%BF%E7%94%A8Python%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83.md>

> python 的虚拟环境可以为一个 python 项目提供独立的解释环境和依赖

### 安装 virtualenv

> pip 可以配置第三方源：pip install -i https://pypi.douban.com/simple virtualenv
>
> pip install virtualenv

### 创建虚拟环境

> Virtualenv 附带有 pip 安装工具
>
> virtualenv env
>
> 选定 Python 版本：virtualenv -p /usr/local/bin/python3 env
>
> 虚拟环境会依赖系统中的 site packages 没系统中已经安装好的第三方 package 也会安装在虚拟环境中，如果不想依赖这些 package，可以加上参数--no-site-packages 简历虚拟环境
> virtualenv --no-site-packages [虚拟环境名称]

### 启动虚拟环境

> source ./[虚拟环境名称]/bin/activate

### 退出虚拟环境

> deactivate

## 虚拟环境管理工具 virtualenvwrapper

> Virtualenvwrapper 是一个虚拟环境管理工具，它能够管理创建的虚拟环境的位置，并能够方便地查看虚拟环境的名称以及切换到指定的虚拟环境

### 安装（确保 virtualenv 已经安装）

> pip install virtualenvwrapper

## 参考项目：https://github.com/dataabc/weiboSpider

## 风格：https://github.com/zh-google-styleguide/zh-google-styleguide/blob/master/google-python-styleguide/python_style_rules.rst
