# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup


def main():
    filename = "cookie.txt"
    cookie = cookielib.MozillaCookieJar(filename)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    content = opener.open("http://jwgl.hainu.edu.cn/")
    #获取之后会用到的viewstate值
    soup = BeautifulSoup(content.read(), 'lxml')
    viewState = soup.input["value"]
    cookie.save(ignore_discard=True, ignore_expires=True)
    res = opener.open("http://jwgl.hainu.edu.cn/CheckCode.aspx")
    data = res.read()
    f = open("checkcode.gif", "wb")
    f.write(data)
    f.close()
    #输入验证码
    checkCodeResult = raw_input("please input the checkcode:")
    _login(opener, viewState, checkCodeResult)

def _login(opener, viewState, checkCodeResult):
    #模拟登陆
    values = {}
    values['__VIEWSTATE'] = viewState
    values['txtUserName'] = '20121613310026'
    values['TextBox2'] = 'ly2625845'
    values['txtSecretCode'] = checkCodeResult
    values['RadioButtonList1'] = '学生'
    values['Button1'] = 'ly2625845'
    values['lbLanguage'] = 'ly2625845'
    values['hidPdrs'] = 'ly2625845'
    values['hidsc'] = 'ly2625845'
    data = urllib.urlencode(values)
    url = 'http://jwgl.hainu.edu.cn/Default2.aspx'
    request = urllib2.Request(url, data)
    response = opener.open(request)
    print response.read()

if __name__ == '__main__':
    main()
