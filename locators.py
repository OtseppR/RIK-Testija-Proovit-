from selenium.webdriver.common.by import By

class MainPageLocators(object):
    #Pealehe lokaatorid
    SEARCH_BUTTON = (By.ID, 'edit-submit')
    LINK_BUTTON = (By.LINK_TEXT, 'e-äriregister')

class SearchResultsPageLocators(object):
    #Otsingu lehe lokaatorid
    OTSITAV_LINK = 'Abieluvararegister'