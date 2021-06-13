from WIN10.API.test_api_case.cookie import *
import pytest
import requests
import allure
import random
from WIN10.API.test_utli.test_yaml_utli import YamlUtli
@allure.feature('第一轮api回归登入测试')
@pytest.mark.parametrize('value',YamlUtli('D:/Python/WIN10/API/test_yaml/test_yaml.yaml').read_yaml())
class Testapp_1:
    @allure.story('产品模块')
    def test_parametrize2(self,value):
        allure.dynamic.description(value['description'])
        allure.dynamic.title(value['title'])

        with allure.step(value['name']):
            url = value['class'][0]['url']
            data = {
                'name':value['class'][0]['name'],
                'code':value['class'][0]['code']
            }
            for i in list(data.keys()):
                if data[i] == 'time':
                    tt = random.randint(000000, 999999)
                    data[i] = tt
            req = requests.post(url,data=data,headers=header,cookies=cookie)
            print(req.json())

        with allure.step(value['jianyan']):
            if 'success' == req.json()['result']:
                assert value['class'][0]['dy'] in req.json()['message']

            elif 'name' in req.json()['message']:
                assert value['class'][0]['dy'] in req.json()['message']['name']

            elif 'code' in req.json()['message']:
                assert value['class'][0]['dy'] in req.json()['message']['code']
