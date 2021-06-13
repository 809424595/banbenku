# import pytest
# import allure
# from time import sleep
# from selenium import webdriver
# from WIN10.TP.test_po.test_po import *
# from WIN10.TP.test_utli.test_yaml_utli2 import YamlUtli2
# @allure.feature('第一轮回归登入测试')
# @pytest.mark.parametrize('value',YamlUtli2('D:/Python/WIN10/TP/test_yaml/test_yaml.yaml').read_yaml())
# class Test_UI():
#
#     def setup_class(self):
#         print('开始测试')
#         with allure.step('打开浏览器'):
#             self.driver = webdriver.Chrome()
#             self.driver.maximize_window()
#
#     @allure.story('下载')
#     def test_dengru(self,value):
#         print(value)
#         # print(value['class'][0]['step'])
#         allure.dynamic.title(value['title'])  #登入成功或登入失败
#         allure.dynamic.description(value['description'])  #描述
#
#
#
#         with allure.step(value['class'][0]['step']):
#             self.driver.get(value['class'][0]['url'])
#
#         with allure.step(value['class'][1]['step']):
#             self.driver.find_element_by_xpath(username).send_keys(value['class'][1]['username'])
#
#         with allure.step(value['class'][2]['step']):
#             self.driver.find_element_by_xpath(password).send_keys(value['class'][2]['password'])
#
#         with allure.step(value['class'][3]['step']):
#             self.driver.find_element_by_xpath(verify).send_keys(value['class'][3]['verify'])
#
#         self.driver.implicitly_wait(10)
#         with allure.step(value['class'][4]['step']):
#             self.driver.find_element_by_xpath(value['class'][4]['login']).click()
#
#
#         with allure.step(value['class'][5]['step']):
#             if 'text'== value['class'][5]['fangfa']:
#                 yy = self.driver.find_element_by_link_text(value['class'][5]['dingwei'])
#                 assert value['class'][5]['dy'] in yy.text
#
#             elif 'xpath'== value['class'][5]['fangfa']:
#                 yy = self.driver.find_element_by_xpath(value['class'][5]['dingwei'])
#                 assert value['class'][5]['dy'] in yy.text
#         with allure.step('用例截图'):
#             allure.attach(self.driver.get_screenshot_as_png(),'用例截图',attachment_type=allure.attachment_type.PNG)
#
#
#
#     def teardown_class(self):
#         print('关闭测试')
#         with allure.step('关闭浏览器'):
#             self.driver.quit()
