import unittest
import pytest
from pages.LoginScreen import LoginScreen
from pages.MainScreen import MainPage


@pytest.mark.usefixtures("beforeClass")
class StartOtmTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.loginScreen = LoginScreen(self.driver)
        self.mainScreen = MainPage(self.driver)

    def test_startSafeBro(self):
        loginPage = self.loginScreen
        mainPage = self.mainScreen
        loginPage.verifyLoginPage()
        loginPage.clickLocalLoginButton()
        loginPage.clickLocationPopUpOk()
        loginPage.clickPermission()
        loginPage.clickLocation()
        loginPage.selectAllowAllTime()
        loginPage.navigateBack()
        loginPage.navigateBack()
        loginPage.navigateToApp()
        mainPage.clickConnectToggle()
        mainPage.clickConnectSafeBro()
        mainPage.verifySafeBroIsOn()
