from element import BasePageElement
from locators import *

class SearchTextElement(BasePageElement):
    #Otsinguvälja lokaator
    locator = 'search_block_form'


class BasePage(object):
    #Class initseerimiseks

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    #Class hoidmaks pealehel tehtavate liigutuste meetodeid

    #Tekitame muutuja, kus hoiame tekstiväljast saadud väärtust
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        #Kinnitamaks, kas pealehe tiitel on korrekne
        return "Registrite ja Infosüsteemide Keskus" in self.driver.title

    def click_search_button(self):
        #Meetod otsingu nupu vajutamiseks
        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()

    def click_link(self):
        #Meetod lingile vajutamiseks
        element = self.driver.find_element(*MainPageLocators.LINK_BUTTON)
        element.click()

    def is_link_title_matches(self):
        #Kinnitamaks, et peale lingile vajutamist on tiitel õige
        return "e-äriregister" in self.driver.title


class SearchResultsPage(BasePage):
    #Class hoidmaks otsingute lehel tehtavate liigutuste meetodeid

    def is_results_found(self):
        #Otsime kogu lehe koodist ebaõnnestunud otsingu teadaannet
        return "Otsing ei andnud tulemusi" not in self.driver.page_source

    def is_correct_result_found(self):
        #Tagastame, kas otsitav link leidub otsingu lehel
        result = self.driver.find_elements_by_link_text(SearchResultsPageLocators.OTSITAV_LINK)
        print(bool(result))
        return bool(result)