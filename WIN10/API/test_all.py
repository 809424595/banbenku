import pytest
import os
if __name__ == '__main__':
    pytest.main(['-s'])
    os.system('allure generate ./allure-results/ -o ./allure-report --clean')