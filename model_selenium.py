from selenium import webdriver

class ModelSelenium:
    driver = None
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        
    def quit(self):
        self.driver.quit()

    def get_text_by_id(self, id):
        return self.driver.find_element_by_id(id).text