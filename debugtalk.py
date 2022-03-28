import time
import uuid
from httprunner import __version__
from httprunner.response import  ResponseObject


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n

def get_uuid():
    return str(uuid.uuid4())

def sleep(n_secs):
    time.sleep(n_secs)

def getTablenum(resp :ResponseObject) -> int  :
    respList = resp.resp_obj.json()
    listNumber = len(respList['tableList']['list'])
    return listNumber


def getListnum(li :list) -> int :
    print(f'list:------------{li}-----\n----长度：----{len(li)}')
    return len(li)


