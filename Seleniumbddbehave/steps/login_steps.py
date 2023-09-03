from behave import given, when, then
import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import allure
import pytest

password = 'XXXXXX' #ACCOUNT DELETED AFTER NOT USING BY 12 MONTHS

@given ('user is on Poczta Onet website')
def step_start_page(context):
    context.driver.get('http://poczta.onet.pl/')
    time.sleep(5)
    context.driver.save_screenshot('before-rodo.png')
    rodo = context.driver.find_element_by_css_selector('button.cmp-button_button.cmp-intro_acceptAll')

    try:
        rodo.click()
    except ElementClickInterceptedException:
        print("Element RODO not found!")

    if rodo.is_displayed():
        rodo.click()
        
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div[1]/div[2]/div/div[3]/button[2]"))).click()

@when('user fills valid username {username} and valid password {password} and submits it')
def step_set_login_in(context, username, password):
    context.driver.save_screenshot('after-rodo.png')
    time.sleep(7)
    context.driver.find_element_by_id('mailFormLogin').send_keys(username)
    context.driver.find_element_by_id('mailFormPassword').send_keys(password)
    context.driver.find_element_by_class_name('loginButton').click()

    #context.driver.find_element_by_id('mailFormLogin').send_keys('janusz.marowski@onet.pl')
    time.sleep(5)

@then ('User can see email list')
def step_valid_login(context):

    try:
        alert_content = context.driver.find_element_by_css_selector("div.messageContent")
        assert alert_content.text == "Wprowadź poprawny adres e-mail" or "Niepoprawny e-mail lub hasło"
        print(alert_content)
        context.driver.save_screenshot("invalidlogin.png")
    except:
        print("Alert not found")

    print(alert_content)
    context.driver.save_screenshot("screenshot-invalidlogin.png")
    
    context.driver.save_screenshot("screenshot-login.png")
    assert context.driver.find_element_by_css_selector('.styles__ListWrapperStyled-vme1nn-0')
    print("URL successfully Accessed")


