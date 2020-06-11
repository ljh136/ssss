from selenium.webdriver.support.wait import WebDriverWait

class Developer_headlines:
    def __init__(self,driver):
        self.driver = driver
    # 点击
    def click(self,loc):
        self.find_element(loc).click()
    # 输入文字
    def input_text(self,loc,text):
        self.find_element(loc).send_keys(text)

    def find_element(self,loc):
        by = loc[0]
        value = loc[1]
        return WebDriverWait(self.driver,5,1).until(lambda x:x.find_element(by,value))

