# -*- coding: utf-8 -*-
# @Author: Mehaei
# @Date:   2023-08-02 17:13:56
# @Last Modified by:   Mehaei
# @Last Modified time: 2023-08-02 21:23:17
import argparse
import os
import sys


def one_file_total(fpname):
    """
    统计一个文件的注释率
    :param fpname: 文件路径
    """
    with open(fpname, 'r', encoding='utf-8') as f:
        code_lines = 0
        comment_lines = 0
        blank_lines = 0
        is_var = False
        is_comment = False
        for index, line in enumerate(f, start=1):
            line = line.strip()
            if "'''" in line or '"""' in line:
                if "=" in line:
                    is_var = True
                else:
                    if is_var:
                        code_lines += 1
                        is_var = False
                        continue
                    else:
                        if is_comment:
                            comment_lines += 1
                            is_comment = False
                            continue
                        else:
                            is_comment = True
            if is_var:
                code_lines += 1
            elif is_comment:
                comment_lines += 1
            elif not line:
                blank_lines += 1
            elif line.startswith("#"):
                comment_lines += 1
            else:
                code_lines += 1

    print("#"*50)
    print(fpname)
    print("注释: %d" % comment_lines)
    print("空行: %d" % blank_lines)
    print("代码: %d" % code_lines)
    program_lines = comment_lines + code_lines
    print("程序行数: %d" % program_lines)
    comment_rate = comment_lines / program_lines
    print("注释率: {:.2f}%".format(comment_rate * 100))
    print("#"*50)
    return comment_lines, blank_lines, code_lines


# 全局统计变量
tcomment_lines = tblank_lines = tcode_lines = 0


def main(fpname):
    """
    统计脚本入口函数
    :param fpname: 文件或文件夹路径
    """
    global tcomment_lines
    global tblank_lines
    global tcode_lines
    if os.path.isdir(fpname):
        for pname in os.listdir(fpname):
            if pname.startswith("."):
                continue
            fp = f"{fpname}/{pname}"
            if os.path.isdir(fp):
                main(fp)
            if os.path.isfile(fp) and fp.endswith(".py"):
                comment_lines, blank_lines, code_lines = one_file_total(fp)
                tcomment_lines += comment_lines
                tblank_lines += blank_lines
                tcode_lines += code_lines
    elif os.path.isfile(fpname) and fpname.endswith(".py"):
        return one_file_total(fpname)
    else:
        print(f"fpname: {fpname}不是文件夹也不是py文件")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="文件注释率统计脚本")
    parser.add_argument('-p', dest='path', type=str, default="./", help="要检测的文件或文件路径")
    args = parser.parse_args()
    fpname = args.path
    if not os.path.exists(fpname):
        print(f"文件路径：{fpname}不存在")
        sys.exit(-1)
    main(fpname)
    if tcomment_lines or tblank_lines or tcode_lines:
        print("*"*50)
        print(fpname)
        print("项目总注释：%d" % tcomment_lines)
        print("项目总空行：%d" % tblank_lines)
        print("项目总代码：%d" % tcode_lines)
        program_lines = tcomment_lines + tcode_lines
        print("项目总程序行数: %d" % program_lines)
        comment_rate = tcomment_lines / program_lines
        print("项目总备注率：{:.2f}%".format(comment_rate * 100))
        print("*"*50)

