import pytest
import os


if __name__ == '__main__':
    pytest.main(['-s','./test_app/test_case_app.py'])
    os.system('allure generate ./allure-results/ -o ./allure-report --clean')