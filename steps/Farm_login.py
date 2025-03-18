from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from driver import get_driver
import time

# Initialize driver
def get_driver_instance(context):
    if not hasattr(context, 'driver'):
        context.driver = get_driver()
    return context.driver

@given('I click on Greener Herd app')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Greener Herd"]')
    element.click()
    time.sleep(1)

@then('I see the splash screen')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView')
    time.sleep(5)

@then('I see the Welcome popup')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Welcome to\nGreener Herd')
    time.sleep(2)

@when('I click Continue with Email')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Continue with Email"]')
    element.click()
    time.sleep(2)

@given('I am on the login with email screen')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Login"]')
    time.sleep(2)

@when('I enter a valid email address {email}')
def step_impl(context,email):
    driver = get_driver_instance(context)
    element =  driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="email address"]')
    element.click()
    element.send_keys(email)
    time.sleep(2)

@when('I enter a valid password {password}')
def step_impl(context,password):
    driver = get_driver_instance(context)
    element =  driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="password"]')
    element.click()
    element.send_keys(password)
    time.sleep(2)

@when('I click on Login')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nLogin')
    element.click()
    time.sleep(2)

@given('the user is on the Dashboard page.')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Dashboard')
    time.sleep(2)

@when("the I clicks on the Menu button.")
def step_impl(context):
    driver = get_driver_instance(context)
    menu = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[4]')
    time.sleep(2)
    menu.click()
    time.sleep(2)

@when("the I clicks on the My Profile button.")
def step_impl(context):
    driver = get_driver_instance(context)
    myProfile = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "My Profile")
    myProfile.click()
    time.sleep(2)

@when("the I clicks on the Complete Profile Now button.")
def step_impl(context):
    driver = get_driver_instance(context)
    completeProfileNow = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "on_tap\nComplete Profile Now")
    completeProfileNow.click()
    time.sleep(2)



@when("the I click and enters a new name {name} in the First Name field.")
def step_impl(context,name):
    driver = get_driver_instance(context)
    firstNameField = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="first name"]')
    time.sleep(2)
    firstNameField.click()
    time.sleep(2)
    firstNameField.clear()
    time.sleep(2)
    firstNameField.send_keys(name)
    time.sleep(2)
    driver.hide_keyboard()
    time.sleep(2)

@when('I scroll down the screen')
def step_impl(context):
    driver = context.driver
    # Use execute_script to perform a mobile scroll
    def scroll_down():
        driver.execute_script("mobile: scrollGesture", {
            "left": 100, "top": 100, "width": 200, "height": 1200,
            "direction": "down",
            "percent": 6.0
        })
    scroll_down()
    time.sleep(5)

@then("the I clicks on the Save button to save the changes.")
def step_impl(context):

    driver = get_driver_instance(context)
    time.sleep(3)

    save = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap\nSave')
    time.sleep(2)
    save.click()
    time.sleep(2)

