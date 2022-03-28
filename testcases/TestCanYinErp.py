
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseERPAddtable(HttpRunner):

    config = (
        Config("testcase description")
        .verify(False)
        .base_url("http://${host}")
        .variables(**{
            "host":"partner.dev.sedsy.com",

            "tableCode":"newtable02"
        })
    )

    teststeps = [
        Step(
            RunRequest("/partner/login")
            .with_variables(**{
                "account": '13311111110',
                "password": '123456'
            })
            .post("/partner/login")
            .with_headers(
                **{
                    "Host": "${host}",
                    "Content-Length": "83",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "X-Requested-With": "XMLHttpRequest",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
                    "token": "null",
                    "requestId": "2022032415230373854685",
                    "Origin": "/",
                    "Referer": "/login.html",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Cookie": "mailver=mail; isAllwayHttps=0",
                    "Connection": "keep-alive",
                }
            )
            .with_cookies(**{"mailver": "mail", "isAllwayHttps": "0"})
            .with_data(
                {
                    "username": "${account}",
                    "password": "${password}",
                    "captcha": "",
                    "uuid": "${get_uuid()}",
                }
            )
            .teardown_hook("${sleep(1)}")  # 调用第三方无返回值的方法
            .extract()      # 获取返回值 前缀
            .with_jmespath('body.token',"tonken") # 获取  返回的tonken 实行参数化
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.msg", "SUCCESS")

        ),

        Step(
            RunRequest("/partner/partnermenu/nav")
            .get("/partner/partnermenu/nav")
            .with_params(**{"_": "1648106587387"})
            .with_headers(
                **{
                    "Host": "${host}",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "X-Requested-With": "XMLHttpRequest",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
                    "token": "$tonken",
                    "requestId": "20220324152307403783841",
                    "Referer": "/index.html",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Cookie": "mailver=mail; isAllwayHttps=0",
                    "Connection": "keep-alive",
                }
            )
            .with_cookies(**{"mailver": "mail", "isAllwayHttps": "0"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.msg", "SUCCESS")
            .assert_equal("body.storeType", 1)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/partner/user/info")
            .get("/partner/user/info")
            .with_params(**{"_": "1648106587388"})
            .with_headers(
                **{
                    "Host": "${host}",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "X-Requested-With": "XMLHttpRequest",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
                    "token": "$tonken",
                    "requestId": "20220324152307403783841",
                    "Referer": "/index.html",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Cookie": "mailver=mail; isAllwayHttps=0",
                    "Connection": "keep-alive",
                }
            )
            .with_cookies(**{"mailver": "mail", "isAllwayHttps": "0"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.msg", "SUCCESS")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/partner/user/nav")
            .get("/partner/user/nav")
            .with_params(**{"_": "1648106587389"})
            .with_headers(
                **{
                    "Host": "${host}",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "X-Requested-With": "XMLHttpRequest",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
                    "token": "$tonken",
                    "requestId": "20220324152307403783841",
                    "Referer": "/index.html",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Cookie": "mailver=mail; isAllwayHttps=0",
                    "Connection": "keep-alive",
                }
            )
            .with_cookies(**{"mailver": "mail", "isAllwayHttps": "0"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.msg", "SUCCESS")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/depot/listStoreUnReadMsg")
            .get("/depot/listStoreUnReadMsg")
            .with_params(**{"_": "1648106587390"})
            .with_headers(
                **{
                    "Host": "${host}",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "X-Requested-With": "XMLHttpRequest",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
                    "token": "$tonken",
                    "requestId": "20220324152307403783841",
                    "Referer": "/index.html",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Cookie": "mailver=mail; isAllwayHttps=0",
                    "Connection": "keep-alive",
                }
            )
            .with_cookies(**{"mailver": "mail", "isAllwayHttps": "0"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.msg", "没有权限，请联系管理员授权")
            .assert_equal("body.code", 500)
        ),
        Step(
            RunRequest("/partner/charts/statistics.json")
            .post("/partner/charts/statistics.json")
            .with_headers(
                **{
                    "Host": "${host}",
                    "Content-Length": "0",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "X-Requested-With": "XMLHttpRequest",
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
                    "token": "$tonken",
                    "requestId": "20220324152307777000684",
                    "Origin": "/",
                    "Referer": "/modules/welcome/partner_welcome.html",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Cookie": "mailver=mail; isAllwayHttps=0",
                    "Connection": "keep-alive",
                }
            )
            .with_cookies(**{"mailver": "mail", "isAllwayHttps": "0"})
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)

        ),
        Step(
            RunRequest("/table/query")
                .get("/table/query")
                .with_params(**{
                    "_": "1648433847905",
                    "page":1,
                    "limit":10,
                    "tableCode":None,
                    "tableStatus":None,
                    "box":None
                    })
                .with_headers(
                **{
                    "Host": "${host}",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "X-Requested-With": "XMLHttpRequest",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
                    "token": "$tonken",
                    "requestId": "${get_uuid()}",
                    "Referer": "/index.html",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Cookie": "mailver=mail; isAllwayHttps=0",
                    "Connection": "keep-alive",
                }
            )
                .teardown_hook("${getTablenum($response)}","tablenum")  #调用三方函数 在响应值中算出数量

                .extract()
                .with_jmespath("body.tableList.totalCount","totalCount") #获取桌台
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_less_or_equals("$tablenum",'$totalCount')   #断点 小于等于

        # ),
        # Step(
        #     RunRequest("/table/add")
        #
        #         .post("/table/add")
        #         .with_headers(
        #         **{
        #             "Host": "partner.dev.sedsy.com",
        #             "Content-Length": "141",
        #             "Accept": "application/json, text/javascript, */*; q=0.01",
        #             "X-Requested-With": "XMLHttpRequest",
        #             "Content-Type": "application/json",
        #             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
        #             "token": "$tonken",
        #             "requestId": "${get_uuid()}",
        #             "Origin": "/",
        #             "Referer": "/modules/merchant/tablemanagement.html",
        #             "Accept-Encoding": "gzip, deflate",
        #             "Accept-Language": "zh-CN,zh;q=0.9",
        #             "Cookie": "mailver=mail; isAllwayHttps=0",
        #             "Connection": "keep-alive",
        #         }
        #     )
        #         .with_cookies(**{"mailver": "mail", "isAllwayHttps": "0"})
        #         .with_json(
        #         {
        #             "tableCode": "${tableCode}",
        #             "tableStatus": 1,
        #             "tableType": 1,
        #             "box": "824241541986373633",
        #             "repastStatus": 2,
        #             "maxCustomer": "50",
        #             "codeUrl": "",
        #             "minPrice": "06",
        #         }
        #     )
        #         .validate()
        #         .assert_equal("status_code", 200)
        #         .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
        #         .assert_equal("body.msg", "SUCCESS")
        #         .assert_equal("body.code", 0)
        )
    ]

if __name__ == "__main__":
    TestCaseERPAddtable().test_start()