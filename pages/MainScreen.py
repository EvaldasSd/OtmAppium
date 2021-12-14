from allure_commons._allure import step

from base.BasePage import BasePage
import utilities.Logger as Logger


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _connectToggle = "com.speedify.onthemove:id/bttnConnect"
    _safeBroToggle = "com.speedify.onthemove:id/switchSafeBro"
    _menu = ".//android.widget.ImageButton[@content-desc='Navigate up']"
    _signOut = "Sign Out"
    _textSafeBroStatusOn = "Safe browsing is initialized: true."

    @step
    def clickConnectToggle(self):
        self.clickElement(self._connectToggle, "id")

    @step
    def clickConnectSafeBro(self):
        self.clickElement(self._safeBroToggle, "id")
        Logger.allureLogs("Toggle safe browsing")

    @step
    def clickMenu(self):
        self.clickElement(self._menu, "xpath")
        Logger.allureLogs("Open menu")

    @step
    def signOut(self):
        self.clickElement(self._signOut, "text")
        Logger.allureLogs("Sign out")

    @step
    def verifySafeBroIsOn(self):
        element = self.isDisplayed(self._textSafeBroStatusOn, "text")
        assert element == True
        Logger.allureLogs("Verify if safebro is on")
