# coding=utf-8
import os
import traceback


class CheckEnvironment:
    """
    查找是否安装所需的环境
    类内函数返回值说明：
    -1 ： 用户终止了操作
    0 ：程序正常返回值
    1 ：程序出现异常
    """
    check_item = None
    check_type = None
    check_instructions = None
    install_instructions = None

    def __init__(self, check_item, check_type):
        """
        :param check_item: 要检查的软件或组件名字
        :param check_type: yum pip ali_sdk
        """
        self.check_item = check_item
        self.check_type = check_type

    def check(self):
        """
        使用yum或pip命令检查对应的软件或组件是否存在，如果不存在进行安装
        :return:
        """
        self.generate_instructions()
        val = os.popen(self.check_instructions).read()
        if val == '':
            i = 0  # 判断是否退出循环
            while i == 0:
                print "检测到未安装", self.check_item, ",缺乏该软件或组件会导致本程序无法正常运行，是否安装？",
                user_input = raw_input("(Y/N):")
                user_input = user_input.lower()
                if user_input == "yes" or user_input == "y":
                    print "正在安装"
                    i = 1
                    res = os.system(self.install_instructions)
                    if res == 0:
                        print "安装成功"
                        return 0
                    else:
                        print "安装失败"
                        return 1
                elif user_input == "no" or user_input == 'n':
                    print "取消安装"
                    return -1
                else:
                    print "非法输入"

    def generate_instructions(self):
        if self.check_type == "yum":
            self.check_instructions = "yum list installed | grep " + self.check_item
            self.install_instructions = "yum install -y " + self.check_item
        elif self.check_type == "pip":
            self.check_instructions = "pip list | grep " + self.check_item
            self.install_instructions = "pip install " + self.check_item
        elif self.check_type == "ali_sdk":
            self.check_instructions = "pip list | grep " + self.check_item
            self.install_instructions = "python " + self.check_item + "/setup.py install"
        else:
            raise Exception("传入的check_type不正确")

