from appium import webdriver

driver ={
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "laurel_sprout",
  "automationName": "UiAutomator1",
  "appPackage": "com.google.android.calculator",
  "appActivity": "com.android.calculator2.Calculator"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)
