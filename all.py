import os
import pytest

if __name__== "__main__" :
    _name="RAIN"
    pytest.main()
    os.system('allure generate ./temp -o ./reports --clean')

