def get_des_cap():
    des_cap = {
        "platformName": "Android", 
        "platformVersion": "11", 
        "appium:deviceName": "emulator-5554",  
        "appium:automationName": "UiAutomator2", 
        "appium:appPackage": "com.example.florales",  
        "appium:appActivity": ".MainActivity",  
        "appium:app": "https://my-app-apks.s3.amazonaws.com/app-debug.apk",  # URL de S3
        "noReset": "true",  
        "appWaitForLaunch": "false", 
        "newCommandTimeout": "120",
        "autoAcceptAlerts": "true"
    }
    return des_cap
