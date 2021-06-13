import pytest
import allure
import os
from appium import webdriver
from time import sleep
from WIN10.APP_QQ_login.test_utli.test_yaml_utli import YamlUtli
from WIN10.APP_QQ_login.peizhi.test_peizhi import *
@allure.feature('第一轮回归登入测试')
@pytest.mark.parametrize('value', YamlUtli('D:/Python/WIN10/APP_QQ_login/test_yaml/test_yaml.yaml').read_yaml())
class TestApp():
    def setup_class(self):
        '''

        :return:
        '''
        pass
    @allure.story('登入模块')
    def test_app(self,value):
        allure.dynamic.title(value['title'])  # 登入成功或登入失败
        allure.dynamic.description(value['description'])  # 描述

        with allure.step('打开QQ'):
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',peizhi)
            self.driver.implicitly_wait(20)
        with allure.step(value['class'][0]['step']):
            self.driver.find_element_by_id(value['class'][0]['login0']).click()

        with allure.step(value['class'][1]['step']):
            self.driver.find_element_by_accessibility_id(name).click()
            self.driver.find_element_by_accessibility_id(name).send_keys(value['class'][1]['name'])

        with allure.step(value['class'][2]['step']):
            self.driver.find_element_by_accessibility_id(passwod).click()
            self.driver.find_element_by_accessibility_id(passwod).send_keys(value['class'][2]['password'])

        with allure.step(value['class'][3]['step']):
            self.driver.find_element_by_accessibility_id(value['class'][3]['login']).click()

        with allure.step(value['class'][4]['step']):
            self.driver.find_element_by_accessibility_id(value['class'][4]['logki']).click()

        with allure.step(value['class'][3]['step']):
            self.driver.find_element_by_accessibility_id(value['class'][3]['login']).click()

        with allure.step(value['class'][5]['step']):
            tt = self.driver.find_element_by_id(value['class'][5]['dingwei'])
            try:
                assert value['class'][5]['dy'] == tt.text
            except Exception as E:
                with allure.step('用例截图'):
                    allure.attach(self.driver.get_screenshot_as_png(), '用例截图',attachment_type=allure.attachment_type.PNG)
                    raise E

    def teardown_class(self):
        with allure.step('关闭QQ'):
            self.driver.quit()
