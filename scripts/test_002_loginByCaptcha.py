#coding:utf-8
import time,allure,random
from Pages.page import Page
from base.base_driver import Base
#from base.base_analyze import analyze_file
import pandas as pd
from sqlalchemy import create_engine
phone = 10000000000 + random.randint(1, 500)
#此处填入数据库连接
engine = create_engine('mysql+pymysql://timing_read_only:db_only_hsyt21@rr-bp12u85w22spt5976do.mysql.rds.aliyuncs.com:3306/timing?charset=utf8')

class Test_loginByCaptcha():
    #setup函数是在一个类里面最先被调用的函数，而且每执行完一个函数都要从setUp()调用开始后再执行下一个函数，有几个函数就调用他几次，与位置无关，随便放在那里都是他先被调用。
    #放一些准备的工作，或者准备一些测试数据。
    def setup(self):
        self.driver = Base().init_driver()
        #设定全局等待
        self.driver.implicitly_wait(50)
        self.page = Page(self.driver)
    #tearDown(）函数是在众多函数执行完后他才被执行，意思就是不管这个类里面有多少函数，他总是最后一个被执行的，与位置无关，最后不管测试函数是否执行成功都执行tearDown()方法；如果setUp()方法失败，则认为这个测试项目失败，不会执行测试函数也不执行tearDown()方法。
    #当我在测试完的时候我要对测试有一个销毁的过程比如说关闭浏览器，那么我们就写在tearDown当中
    def teardown(self):
        self.driver.quit()
    #判断元素是否在当前页面内
    sourse = []
    # @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_address"))                               # 装饰器
    #手机号密码登录测试用例
    def test_loginByCaptcha(self):
        with allure.step('点击同意服务协议'):
            self.page.login().click_agree_login()
        with allure.step('点击手机号登录'):
            self.page.login().click_phone_login()
        with allure.step('输入手机号'):
            self.page.login_phone().input_phone(str(phone))
        with allure.step('点击获取验证码按钮'):
            self.page.login_phone().click_getCaptcha()
            time.sleep(2)
        with allure.step('正式服数据库拿验证码'):
            captcha = pd.read_sql('select captcha FROM t_captcha WHERE phone = "' + str(phone) + '" order by postTime desc',engine)
            captcha = captcha.iloc[0, 0]
        with allure.step('输入验证码'):
            self.page.login_phone_captcha().input_captcha(str(captcha))
        with allure.step('点击完成'):
            self.page.login_phone_captcha().click_loginBtn()
        with allure.step('断言:看到学习圈按钮-->登录成功'):
            assert self.page.shouye().check_friendCircle() == True

    def test_logout(self):
        with allure.step('点击更多按钮'):
            time.sleep(5)
            self.page.shouye().click_mainMoreBtn()
        with allure.step('点击设置按钮'):
            self.page.more().click_settingBtn()
        with allure.step('点击退出登录按钮'):
            self.page.setting().click_logout()
        with allure.step('确定退出'):
            self.page.setting().click_confirmLogout()
            time.sleep(2)
        with allure.step('断言:退出登录成功'):
            assert self.page.login().check_loginByphone() == True
