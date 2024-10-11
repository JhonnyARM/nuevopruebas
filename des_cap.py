def get_des_cap():
    des_cap = {
        "platformName": "Android", 
        "platformVersion": "11", 
        "appium:deviceName": "emulator-5554",  
        "appium:automationName": "UiAutomator2", 
        "appium:app": "bs://484f79f7cc8697b9bab640a22cf819e63886aee2",  # URL de BrowserStack
        "noReset": "true",  
        "appWaitForLaunch": "false", 
        "newCommandTimeout": "120",
        "autoAcceptAlerts": "true"
    }
    return des_cap
