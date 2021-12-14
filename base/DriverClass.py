from appium import webdriver


class Driver:

    def getDriver(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '11',
            'deviceName': 'Galaxy A42 5G',
            'app': ('/Users/apps/OnTheMove-287.apk'),
            'appPackage': 'com.speedify.onthemove',
            'appActivity': 'com.speedify.onthemove.LoginActivity'
        }

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver