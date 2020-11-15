from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
import json
import configparser
import time


def getRequestId():
    cf = configparser.ConfigParser()
    cf.read("user.conf", encoding='utf-8')
    AccessKey_ID = cf.get("AccessKey", "AccessKey_ID")
    AccessKey_Secret = cf.get("AccessKey", "AccessKey_Secret")
    DomainName = cf.get("DDNS", "set_DomainName")
    client = AcsClient(AccessKey_ID, AccessKey_Secret, 'cn-hangzhou')
    request = DescribeDomainRecordsRequest()
    request.set_accept_format('json')
    request.set_DomainName(DomainName)
    response = client.do_action_with_exception(request)
    json2dict = json.loads(response)
    DomainRecords = json2dict['DomainRecords']
    Record = DomainRecords['Record']
    print Record
    RecordId = Record[0]['RecordId']
    return RecordId
    # print(str(response, encoding='utf-8'))


def UpdateDomainRecord(RequestId, IP):
    cf = configparser.ConfigParser()
    cf.read("user.conf", encoding='utf-8')
    AccessKey_ID = cf.get("AccessKey", "AccessKey_ID")
    AccessKey_Secret = cf.get("AccessKey", "AccessKey_Secret")
    rr = cf.get("DDNS", "RR")
    type = cf.get("DDNS", "Type")
    sleep_time = cf.get("frequency", "time")
    time.sleep(sleep_time)
    client = AcsClient(AccessKey_ID, AccessKey_Secret, 'cn-hangzhou')

    request = UpdateDomainRecordRequest()
    request.set_accept_format('json')

    request.set_RecordId(RequestId)
    request.set_RR(rr)
    request.set_Type(type)
    request.set_Value(IP)

    response = client.do_action_with_exception(request)
    return response
    # python2:  print(response)
    #print(str(response, encoding='utf-8'))

