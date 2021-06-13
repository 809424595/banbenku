import pytest
import os

if __name__ == '__main__':
    pytest.main(['D:/Python/WIN10/TP/test_tpui/test_case.py'])
    os.system('allure generate ./allure-results/ -o ./allure-report --clean')