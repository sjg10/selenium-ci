import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", required=True, help="URL under test"
    )

# this method here makes your configuration global
option = None
def pytest_configure(config):
    global option
    option = config.option

def get_url():
    return option.url

def get_driver():
    options = webdriver.ChromeOptions()    
    options.add_argument("--headless=new")
    return webdriver.Chrome(options = options)