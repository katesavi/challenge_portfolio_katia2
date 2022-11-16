import os
import time
import unittest

from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from pages.add_page import AddPage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayerButton(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player_button(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        new_player = AddPage(self.driver)
        new_player.title_of_page()
        new_player.type_in_name('Pat')
        new_player.type_in_surname('Mat')
        new_player.type_in_phone('+4877777777777')
        new_player.type_in_weight('80')
        new_player.type_in_email('greengrass@gmail.com')
        new_player.type_in_click_the_submit_button()
        new_player.type_in_level('1')
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
