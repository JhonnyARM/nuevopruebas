def get_des_cap():
    des_cap = {
        "platformName": "Android",
        "platformVersion": "11",
        "appium:deviceName": "Samsung Galaxy S20",  # Cambia a un dispositivo que desees usar
        "appium:automationName": "UiAutomator2",
        "appium:app": "bs://484f79f7cc8697b9bab640a22cf819e63886aee2",  # ID de tu app en BrowserStack
        "noReset": "true",
        "appWaitForLaunch": "false",
        "newCommandTimeout": "120",
        "autoAcceptAlerts": "true",
        "browserstack.user": "",  # Se dejará vacío
        "browserstack.key": ""     # Se dejará vacío
    }
    return des_cap
