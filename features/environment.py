from selenium import webdriver


def before_scenario(context, scenario):
    print(scenario.name, 'started')
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    context.browser = webdriver.Chrome(chrome_options=options)
    context.browser.get('http://www.facebook.com/')


def after_scenario(context, scenario):
    context.browser.quit()
    print(scenario.name, 'finished')
