from selenium import webdriver
import selenium

def before_scenario(context,scenario):
    #context.driver = webdriver.Chrome()
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(3)

def after_scenario(context,scenario):
    print(context.driver.get_cookies())
    context.driver.delete_all_cookies()
    context.driver.quit()



