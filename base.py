# base.py
# -*- coding: utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import cookielib

_user_info = {
    'name': '',
    'username': '',
    'password': ''
}


def _login():
    # 先得到出cookie和viewstate的值再进行访问
    print ">>> step01 <<<"
    url = "http://jwgl.hainu.edu.cn/"
    viewstate = {'name': '', 'value': ''}
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(url)
    if response.code != 200:
        return False
    else:
        soup = BeautifulSoup(response.read(), "lxml")
        if not len(soup.select('input[name="__VIEWSTATE"]')):
            return False
        else:
            input = soup.select('input[name="__VIEWSTATE"]')[0]
    viewstate['name'] = input['name']
    viewstate['value'] = input['value']
    if len(cookie) == 0 or viewstate['name'] == '' or viewstate['value'] == '':
        return False
    print 'url>>', url
    print 'viewstate>>', viewstate
    print 'cookie>>', cookie

    # 开始模拟登陆教务系统，尝试不要验证码
    print '>>>step 02<<<'
    url = 'http://jwgl.hainu.edu.cn/'
    postdata = urllib.urlencode({
        '__VIEWSTATE': viewstate['value'],
        'txtUserName': '20121613310026',
        'TextBox2': 'ly2625845',
        'txtSecretCode': '',
        'RadioButtonList1': '学生',
        'Button1': '',
        'lbLanguage': '',
        'hidPdrs': '',
        'hidsc': ''
    })
    print 'postdata >>', postdata
    requset = urllib2.Request(url=url, data=postdata)
    # argvs   sub
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(requset)
    if response.code == 302:
        print '>>analog login success, response code = ', response.code
        print response.code
        return True
    else:
        print '>>analog login fail, response.code = ', response.code
        return False


def _analyze(argvs):
    '''extract the target info'''
    _user_info['name'] = 'XX'
    pass


def sendtable2user(email_addr):
    '''send talbe data to someone'''
    pass


def _test():
    flag = _login()
    if flag:
        print 'login success'
    else:
        print 'login fail'
    pass

if __name__ == '__main__':
    _test()
