# Python

## 术语

- `模块：`尽量使用小写命名，decoder、html_parser 等
- `类名：`首字母大写，大驼峰
- `函数：`小写，下划线
- `变量名：`小写，下划线
- `常量：`大写，下划线
- `注释`：#后空格，段落使用空注释行

## 工具集

### pip 包管理工具

### pipenv：官方推荐的新包管理工具

> 集成了 safety 模块，pipenv check
>
> 集成了 flake8 模块，检测编码风格，pipenv check --style test.py
>
> 指定python版本，pipenv --python3.6

### virtualenv 虚拟环境工具

### pyenv Python 版本管理工具

## Python 虚拟环境 virtualenv<https://github.com/walter201230/Python/blob/master/Article/advanced/%E4%BD%BF%E7%94%A8Python%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83.md>

> python 的虚拟环境可以为一个 python 项目提供独立的解释环境和依赖
>
> virtualenv 包用于创建 Python 虚拟环境
>
> Pyhton@3.3以后，内置了 venv module，实现了 virtualenv 的部分功能
>
> pipenv 是 Python 官方推荐 的包管理工具。可以说，它集成了 virtualenv, pip 和 pyenv 三者的功能。其目的旨在集合了所有的包管理工具的长处，如: npm, yarn, composer 等的优点。它能够自动为项目创建和管理虚拟环境，从 Pipfile 文件添加或删除安装的包，同时生成 Pipfile.lock 来锁定安装包的版本和依赖信息，避免构建错误。

### 安装 virtualenv

> pip 可以配置第三方源：pip install -i https://pypi.douban.com/simple virtualenv
>
> pip install virtualenv

#### 创建虚拟环境

> Virtualenv 附带有 pip 安装工具
>
> virtualenv env
>
> 选定 Python 版本：virtualenv -p /usr/local/bin/python3 env
>
> 虚拟环境会依赖系统中的 site packages 没系统中已经安装好的第三方 package 也会安装在虚拟环境中，如果不想依赖这些 package，可以加上参数--no-site-packages 简历虚拟环境
> virtualenv --no-site-packages [虚拟环境名称]

#### 启动虚拟环境

> source ./[虚拟环境名称]/bin/activate

#### 退出虚拟环境

> deactivate

### Python@3.3自带 venv 模块<https://docs.python.org/3/library/venv.html>

```js
/*
    pyvenv.cfg中的，home指定python；version指定版本
    创建虚拟环境：python3 -m venv mysite/env
    激活虚拟环境：source mysite/env/bin/activate
 */
```

### pipenv 是官方推荐的包管理工具，集成了 virtualenv、pip 和 pyenv 的功能。类似 npm 等工具

<https://packaging.python.org/en/latest/tutorials/managing-dependencies/#managing-dependencies>

```js
/*
pipenv主要解决了如下问题:

不用再单独使用pip和virtualenv, 现在它们合并在一起了
不用再维护requirements.txt, 使用Pipfile和Pipfile.lock来代替
可以使用多个python版本(python2和python3)
在安装了pyenv的条件下，可以自动安装需要的Python版本
安装pipenv：pip install pipenv -i https://pypi.douban.com/simple
*/
```

## 虚拟环境管理工具 virtualenvwrapper

> Virtualenvwrapper 是一个虚拟环境管理工具，它能够管理创建的虚拟环境的位置，并能够方便地查看虚拟环境的名称以及切换到指定的虚拟环境

### 安装（确保 virtualenv 已经安装）

> pip install virtualenvwrapper

## 参考项目：https://github.com/dataabc/weiboSpider

## 风格：https://github.com/zh-google-styleguide/zh-google-styleguide/blob/master/google-python-styleguide/python_style_rules.rst
