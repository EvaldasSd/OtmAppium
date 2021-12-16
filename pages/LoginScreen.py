from allure_commons._allure import step
from base.BasePage import BasePage


class LoginScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _localLoginButton = "com.speedify.onthemove:id/bttnLoopbackLogin"
    _loginButton = "com.speedify.onthemove:id/bttnLogin"
    _pagetitle = "Sign In"
    _locationPopUpOk = ".//android.widget.Button[@text='OK']"
    _permissions = "//android.widget.TextView[@text='Permissions']"
    _location = "Location"
    _allowAllTime = "com.android.permissioncontroller:id/allow_always_radio_button"
    _back = "//android.widget.ImageButton[@content-desc='Back']"
    _backToApp = "//android.widget.ImageButton[@content-desc='Navigate up']"

    @step
    def navigateToApp(self):
        self.clickElement(self._backToApp, "xpath")

    @step
    def navigateBack(self):
        self.clickElement(self._back, "xpath")

    @step
    def selectAllowAllTime(self):
        self.clickElement(self._allowAllTime, "id")

    @step
    def clickLocation(self):
        self.clickElement(self._location, "text")

    @step
    def clickPermission(self):
        self.clickElement(self._permissions, "xpath")

    @step
    def clickLocationPopUpOk(self):
        self.clickElement(self._locationPopUpOk, "xpath")

    @step
    def clickLocalLoginButton(self):
        self.clickElement(self._localLoginButton, "id")

    @step
    def clickLoginButton(self):
        self.clickElement(self._loginButton, "id")

    @step
    def verifyLoginPage(self):
        element = self.isDisplayed(self._pagetitle, "text")
        assert element == True
