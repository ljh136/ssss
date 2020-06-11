import os,sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.developer_headlines_page import Developer_headlines_page

class Test_Developer_headlines:
    def setup(self):
        self.driver = init_driver()
        self.dev_headlines_page = Developer_headlines_page(self.driver)

    def test_developer_headlines_fund(self):
        # 点击发现
        self.dev_headlines_page.click_found()
        # 输入框
        self.dev_headlines_page.click_input()
        # 输入文字
        self.dev_headlines_page.input_search_text("CSDN")
        # 退出开发者头条
        self.dev_headlines_page.end_developer()
        self.dev_headlines_page.end_dev()
