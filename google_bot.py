from selenium import webdriver; from selenium.webdriver.common.keys import Keys
class GoogleBot():
    def __init__(self):self.driver = webdriver.Chrome()
    def google(self):self.driver.get('https://www.google.com/')
    def youtube(self):self.driver.get('https://www.youtube.com/')
    def search(self, question): 
        try:self.driver.find_element_by_name("q").send_keys(question, Keys.RETURN)       
        except Exception:self.driver.find_element_by_name("search_query").send_keys(question, Keys.RETURN)
