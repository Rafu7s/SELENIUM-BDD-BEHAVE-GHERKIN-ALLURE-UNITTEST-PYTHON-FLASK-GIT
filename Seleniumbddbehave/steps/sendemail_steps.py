from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

password = 'XXXXXX'  #ACCOUNT DELETED AFTER NOT USING BY 12 MONTHS

@given('user is log on Poczta Onet')
def already_logon(context):
    context.driver.get('http://poczta.onet.pl/')
    time.sleep(3)
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.cmp-button_button.cmp-intro_acceptAll"))).click()
    context.driver.find_element_by_id('mailFormLogin').send_keys('janusz.marowski@onet.pl')
    context.driver.find_element_by_id('mailFormPassword').send_keys(password)
    context.driver.find_element_by_class_name('loginButton').click()

@when('logo is there')
def logo_checking(context):
    time.sleep(3)
    status = context.driver.find_element_by_xpath('/html/body/main/div/header/div[1]/figure/a[1]').is_displayed()
    if status==True:
        assert True
    else:
        assert False

@when('user click button Napisz wiadomosc')
def button_send_clicked(context):
    time.sleep(3)
    context.driver.find_element_by_xpath('/html/body/main/div/div[6]/div[3]/aside/div[1]/div/span').click()

@when('user puts address recipient')
def address_given(context):
    time.sleep(3)

    context.driver.find_element_by_xpath('/html/body/main/div/div[6]/div[3]/div/div[1]/section/div[2]/div[2]/div/div/div/div/input').send_keys('testowe.1979@o2.pl')
    context.driver.save_screenshot('screen.png')
    time.sleep(1)
    context.driver.find_element_by_xpath('/html/body/main/div/div[6]/div[3]/div/div[1]/section/div[2]/div[2]/div/div/div/div[1]/input').click()
    context.driver.save_screenshot('screen4.png')

@when('user puts title of e-mail')
def title(context):
    context.driver.find_element_by_xpath('/html/body/main/div/div[6]/div[3]/div/div[1]/section/div[2]/div[3]/div/div/div/input').send_keys('Wniosek')
    context.driver.save_screenshot('screen2.png')

@when('user puts text of message')
def message(context):
    time.sleep(5)
    context.driver.find_element_by_id('CONTENT_TEXTAREA_ID_ifr').send_keys('Hej, Co u Ciebie? MAsz czas sie spotkac we wtorek, pojdziemy do kina?? Pozdro KArol')
    context.driver.save_screenshot('screen3.png')

@when('user click Wyslij button')
def click_send(context):
    time.sleep(8)
    context.driver.find_element_by_xpath('/html/body/main/div/div[6]/div[3]/div/div[1]/section/div[1]/div/ul[1]/li[2]/button/span/span').click()

@then('User send e-mail to friend')
def send(context):
    assert context.driver.find_element_by_css_selector('.styles__ListWrapperStyled-vme1nn-0')
    print("Email successfully sent")
