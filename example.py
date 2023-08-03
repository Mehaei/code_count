# -*- coding: utf-8 -*-
# @Author: Mehaei
# @Date:   2023-08-02 20:57:42
# @Last Modified by:   Mehaei
# @Last Modified time: 2023-08-03 14:28:30
# 导入模块
import os


# 入口函数
def main():
    """this comment"""
    '''this comment 1'''
    m1 = """this code"""
    m1 = '''this code'''
    msg = """
        message info
    """
    print(msg)
    print(m1)
    print("""this code also""")
    print('''this code also''')
    print(os.getcwd())


# 调用函数
main()
