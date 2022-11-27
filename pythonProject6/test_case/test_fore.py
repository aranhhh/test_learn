import requests
from config.conf import *  # * 模糊导入，导入文件里面所有的函数
from common.get_excel import *
import re
import pytest
url_reg = server_ip()+"/actions/Account.action" #带括号显示，带括号表示引入这个函数，而不是这个方法
# 注册
def test_reg():
    cookies = {
        "JSESSIONID": "DA147B2297A898883D71046C2B464235"
    }
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'cache-control': 'max-age=0',
        'cookie': 'JSESSIONID=DA147B2297A898883D71046C2B464235',
        'referer': 'https://petstore.octoperf.com/actions/Account.action?newAccountForm=',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
    # 发送请求,表单格式的数据，用 data
    r_reg = requests.post(url=url_reg, headers=headers, cookies=cookies)
    # print(r_reg.text)  # 打印的正文内容
    # print(r_reg.status_code)  # 打印返回的状态码
    assert r_reg.status_code == 200

# 登录
def test_login():
    url_login = server_ip() + "/actions/Account.action"
    data = {
        'username': 'aranhhh',
        'password': '123456',
        'signon': 'Login',
        '_sourcePage': '8MN_neU7WcMbL-KmOMGjFY-90BDTRS57gfA622yQ0ReDFw1x_Qklz-nmOVwyKQGsonbGl3RyX0qj72BnP4YT1gsChu7ytRqxTfQHC4-R-i8=',
         '__fp': 'r4tAPnn3Jel3cihKLxRzg8-XQcdG4VHEo9RZrOvvouaOYE3OWGvtyvCvWGO2_K9U'
    }
    r_login = requests.post(url=url_login, data=data)
    # print(r_login.text)
    # print(r_login.url)
    # print(r_login.status_code)
    assert r_login.status_code == 200

# 查询接口
def test_search():
    url_search = server_ip() + '/actions/Catalog.action'
    data = {
        'keyword': '66666',
        'searchProducts': 'Search',
        # '_sourcePage': 'trg_hwK2saEivKQD5hbknVta9ilHErLNy08c_YIu0I0PnLgyYrWwY5dWFgJO1p4ZIRaUWvU_Nkq6s0XY_CDRePaXQ0_Xgz9w',
        # '__fp': 'u4OPHajv2jJ-Da7gGJXwlQ-taFAgZ8BsISUsNRFE4tn_gyO8CuyWJS9mS53EmNmT'
        }
    r_search = requests.post(url=url_search, data=data)
    # print(r_search.text)
    # print(r_search.status_code)
    # print(r_search.url)
    assert r_search.status_code == 200

# 调用excel文件 查询内容
def test_search1():
    url_search2 = server_ip() + '/actions/Catalog.action'
    searchmessage = get_excel_row(2,1)
    data = {
        'keyword': searchmessage,
        'searchProducts': 'Search',
        # '_sourcePage': 'trg_hwK2saEivKQD5hbknVta9ilHErLNy08c_YIu0I0PnLgyYrWwY5dWFgJO1p4ZIRaUWvU_Nkq6s0XY_CDRePaXQ0_Xgz9w',
        # '__fp': 'u4OPHajv2jJ-Da7gGJXwlQ-taFAgZ8BsISUsNRFE4tn_gyO8CuyWJS9mS53EmNmT'
        }
    r_search = requests.post(url=url_search2, data=data)
    # print(r_search.text)
    # print(r_search.status_code)
    # print(r_search.url)
    assert r_search.status_code == 200

# 查询2
def test_search2():
    url_search2 = server_ip() + '/actions/Catalog.action'
    searchmessage = get_excel_row(2, 1)
    data = {
        'keyword': searchmessage,
        'searchProducts': 'Search',
        # '_sourcePage': 'trg_hwK2saEivKQD5hbknVta9ilHErLNy08c_YIu0I0PnLgyYrWwY5dWFgJO1p4ZIRaUWvU_Nkq6s0XY_CDRePaXQ0_Xgz9w',
        # '__fp': 'u4OPHajv2jJ-Da7gGJXwlQ-taFAgZ8BsISUsNRFE4tn_gyO8CuyWJS9mS53EmNmT'
        }
    r_search = requests.post(url=url_search2, data=data)
    # 如何去提取text格式数据的信息，用到re模块，正则表达式
    # url_productid = re.findall('<td>(.*?)</td>',r_search.text)
    # print(url_productid)
    url_productid = re.findall('<td>(.*?)</td>',r_search.text)[1]
    # print(url_productid)
    url_productide =re.findall('<font color="BLACK">(.*?)</font>',url_productid)
    # print(url_productide)
    assert get_excel_row(1, 0) in ''.join(url_productide)
    # assert r_search.status_code == 200
    # print(r_search.text)
    # print(r_search.status_code)
    # print(r_search.url)

