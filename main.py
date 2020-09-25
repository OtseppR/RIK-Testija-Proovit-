# RIK tesija proovitöö tehniline osa
# Variant C
# Autor: Randolf Otsepp

import unittest
from selenium import webdriver
import page

class RIK_EE(unittest.TestCase):

    def setUp(self):
        #Antud testide jooksutamiseks kasutan Google Chrome 85 brauserit ja sellele vastavat driverit, mis
        # asub samas kataloogis
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.rik.ee/")

    def test_title_rik_ee(self):
        #Pealehe laadimine
        main_page = page.MainPage(self.driver)
        #Kontrollime, kas "Registrite ja infosüsteemide keskus" on pealehe tiitliks
        assert main_page.is_title_matches(), "Registrite ja Infosüsteemide Keskuse lehe pealkiri ei ole korrektne"

    def test_search_rik_ee(self):
        """
        Siin testime rik.ee otsingumootorit otsides märksõna "abieluvararegister" järgi.
        Esmalt kontrollime, et vasted ei jääks tühjaks ning seejärel tahame vastetest
        leida korrektse vaste, milleks on link nimega "Abieluregister". Juhul, kui mingil
        punktil ei ole oodatud tulem, siis vastavalt kohale saadab test sellekohase teate.
        """

        main_page = page.MainPage(self.driver)
        #Kirjutame otsinguvälja "abieluvararegister"
        main_page.search_text_element = "abieluvararegister"
        main_page.click_search_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Teeme kindlaks, et leiame vasteid
        assert search_results_page.is_results_found(), "Tulemusi ei leitud"
        #Teeme kindlaks, et leiame õige vaste, milleks on link nimega "Abieluregister"
        assert search_results_page.is_correct_result_found(), "Ei leitud oodatud vastet"

    def test_invalid_search_rik_ee(self):
        #Kontrollime, et kirjutades otsingumootorisse '$$$' ei tule vasteid
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "$$$"
        main_page.click_search_button()
        search_results_page = page.SearchResultsPage(self.driver)
        assert not search_results_page.is_results_found()

    def test_links_rik_ee(self):
        #Kontrollime pealehe linke, vajutades ühele ja uurides, kas suunatud asukoht on õige tiitliga
        main_page = page.MainPage(self.driver)
        main_page.is_link_title_matches(), "Vajutades lingile 'E-ÄRIREGISTER' on avanenud lehe tiitel ebakorrektne"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()