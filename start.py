# coding=utf-8
"""
Create on = 14/11/2020
@author: Disguiser-D
version = 0.1.0
"""

import check
import os

if __name__ == '__main__':
    check.check()
    import main

    while 1:
        RecordId = main.getRequestId()
        print RecordId
        IP = os.popen("curl icanhazip.com").read()
        try:
            res = main.UpdateDomainRecord(RecordId, IP)
        except:
            pass
