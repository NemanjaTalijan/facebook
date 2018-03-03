import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class TestsFacebook(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.get('https://www.facebook.com')

    def testSingIn(self):
        firstNameField = self.browser.find_element_by_name('firstname')
        firstNameField.send_keys('Pera')
        self.assertEqual('Pera', firstNameField.get_attribute('value'))
        lastNameField = self.browser.find_element_by_name('lastname')
        lastNameField.send_keys('Peric')
        self.assertEqual('Peric', lastNameField.get_attribute('value'))
        eMailField = self.browser.find_element_by_name('reg_email__')
        eMailField.send_keys('pera.peric@gmail.com')
        self.assertEqual('pera.peric@gmail.com', eMailField.get_attribute('value'))
        reEnterEMailField = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.NAME, 'reg_email_confirmation__'))
        )
        action = ActionChains(self.browser)
        action.send_keys_to_element(reEnterEMailField, 'pera.peric@gmail.com').perform()
        newPasswordFiled = self.browser.find_element_by_name('reg_passwd__')
        newPasswordFiled.send_keys('password123*')
        self.assertEqual('password123*', newPasswordFiled.get_attribute('value'))
        birthDayMonthField = Select(self.browser.find_element_by_xpath('//*[@id="month"]'))
        birthDayMonthField.select_by_visible_text('Mar')
        birthDayField = Select(self.browser.find_element_by_xpath('//*[@id="day"]'))
        birthDayField.select_by_visible_text('24')
        birthDayYearFiled = Select(self.browser.find_element_by_xpath('//*[@id="year"]'))
        birthDayYearFiled.select_by_visible_text('1988')
        genderPickerRadioButton = self.browser.find_element_by_xpath('//*[@id="u_0_c"]')
        genderPickerRadioButton.click()
        # SubmitButton = self.browser.find_element_by_xpath('//*[@id="u_0_w"]')
        # ActionChains(self.browser).click(SubmitButton).perform()
        time.sleep(2)

    def testLogIn(self):
        emailOrPhoneField = self.browser.find_element_by_xpath('//*[@id="email"]')
        emailOrPhoneField.send_keys('name@gmail.com')
        passwordField = self.browser.find_element_by_xpath('//*[@id="pass"]')
        passwordField.send_keys('password123')
        # logInButton = self.browser.find_element_by_xpath('//*[@id="u_0_2"]')
        # logInButton.click()

    def tearDown(self):
        self.browser.close()


if __name__ == '__main__':
    unittest.main()
