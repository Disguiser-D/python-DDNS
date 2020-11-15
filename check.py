# coding=utf-8

import CheckEnvironment
import os

def check():
    print "正在检查是否安装软件运行所需的环境"
    res_epel = CheckEnvironment.CheckEnvironment("epel-release", "yum")
    res_epel.check()
    val = os.popen("yum -y update").read()
    res_pip = CheckEnvironment.CheckEnvironment("python2-pip.noarch", "yum")
    res_pip.check()
    print "正在检查是否安装软件运行所需的python所需的第三方库"
    res_ali_sdk_core = CheckEnvironment.CheckEnvironment("aliyun-python-sdk-core", "ali_sdk")
    res_ali_sdk_core.check()
    res_ali_sdk_dns = CheckEnvironment.CheckEnvironment("aliyun-python-sdk-alidns", "ali_sdk")
    res_ali_sdk_dns.check()
    res_jmespath = CheckEnvironment.CheckEnvironment("jmespath", "pip")
    res_jmespath.check()
    res_config = CheckEnvironment.CheckEnvironment("configparser", "pip")
    res_config.check()

