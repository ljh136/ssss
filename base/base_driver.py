from appium import webdriver

def init_driver():
    # server 启动参数
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 获取app的设置信息---->开发者头条
    desired_caps['appPackage'] = 'io.manong.developerdaily'
    desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.MainActivity'
    # 写入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # 声明driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
