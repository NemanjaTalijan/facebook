from behave import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


@given('User is on Facebook website')
def step(context):
    print('GIVEN STEP FOR SCENARIO:', context.scenario.name)
    assert 'Facebook - Log In or Sign Up' in context.browser.title
    print(context.browser.title)


@when('User types personal informations: {email} and {password}')
def step(context, email, password):
    if email == '*':
        email = ''
    if password == '*':
        password = ''
    print('GIVEN VALUES FOR EMAIL AND PASSSWORD: ', email, password)
    emailField = context.browser.find_element_by_id('email')
    emailField.send_keys(email)
    passField = context.browser.find_element_by_id('pass')
    passField.send_keys(password)


@when('Clicks on LogIn button')
def step(context):
    loginButton = None
    try:
        loginButton = WebDriverWait(context.browser, 5).until(
        EC.presence_of_element_located((By.ID, 'u_0_2'))
        )
    except TimeoutException:
        print('NoSuchElementFound!')
    action = ActionChains(context.browser)
    action.click(loginButton).perform()


@then('User should get: {massageLink} on site')
def step(context, massageLink):
    wrongUser = None
    wrongPassword = None
    try:
        wrongUser = WebDriverWait(context.browser, 5).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Sign up for an account.'))
        )

        wrongPassword = WebDriverWait(context.browser, 5).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Forgot Password?'))
        )
    except TimeoutException:
        if wrongUser is not None:
            print('User not registered!')
        elif wrongPassword is not None:
            print('Wrong password entered!')
        else:
            print('NoSuchElementFound!')
