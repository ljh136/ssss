import os,sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import Developer_headlines

class Developer_headlines_page(Developer_headlines):
    # 点击发现
    found = By.XPATH,"//*[contains(@text,'发现')]"
    # 输入框
    click_input_text = By.XPATH,"//*[contains(@text,'搜索感兴趣的独家号、文章、标签')]"
    # 输入文字
    input_text_view = By.ID,"io.manong.developerdaily:id/edt_keyword"
    # 退出开发者头条
    end_developer_headlines = By.CLASS_NAME,"android.widget.ImageButton"
    end_dev_headlines = By.CLASS_NAME, "android.widget.ImageButton"

    # 发现
    def click_found(self):
        self.click(self.found)
    # 输入框
    def click_input(self):
        self.click(self.click_input_text)
    # 输入文字
    def input_search_text(self,text):
        self.input_text(self.input_text_view,text)
    # 退出开发者头条
    def end_developer(self):
        self.click(self.end_developer_headlines)
    def end_dev(self):
        self.click(self.end_dev_headlines)
