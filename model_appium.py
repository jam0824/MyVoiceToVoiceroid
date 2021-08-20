from appium import webdriver

class ModelAppium:
    driver = None
    def __init__(self, addr, app_path):
        desired_caps = {}
        desired_caps["app"] = app_path
        self.driver = webdriver.Remote(
            command_executor=addr,
            desired_capabilities=desired_caps)

    def quit(self):
        self.driver.quit()

    def play(self, text):
        el = self.driver.find_element_by_accessibility_id("TextBox")
        el.clear()
        el.send_keys(text)
        self.driver.find_element_by_name("再生").click()