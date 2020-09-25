from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    #Class kus tegutseme pealehel olevate tekstiväljadega

    def __set__(self, obj, value):
        #Muudame teksti antud väärtuseks
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        #Loeme antud objekti sisse ning tagastame selle tekstilise väärtuse
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")