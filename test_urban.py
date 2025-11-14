import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from main import UrbanRoutesPage
from LOCATORS import UrbanRoutesLocators


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        service = Service("/usr/local/bin/chromedriver")
        from selenium.webdriver import DesiredCapabilities

        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        cls.driver = webdriver.Chrome(service=service)

    ## Establecer ruta
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    ### Selecionar comfort
    def test_button_comfort(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_taxi_button()

        routes_page.click_button_comfort()
        assert routes_page.button_comfort_selected() is True

    ### Phone number
    def test_phone_number_and_sms(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_taxi_button()
        routes_page.click_button_comfort()
        routes_page.set_phone_number(data.phone_number)
        routes_page.enter_sms_code()

        assert True

    ### Metodod de pago
    def test_add_credit_card(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_taxi_button()
        routes_page.click_button_comfort()

        routes_page.click_payment_method_button()
        routes_page.add_new_card()

        routes_page.set_card_details(data.card_number, data.card_code)
        routes_page.save_card()

        assert True

    ### Driver message
    def test_write_message_for_driver(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_taxi_button()
        routes_page.click_button_comfort()

        message = "Traiga un aperitivo"
        routes_page.set_message_for_driver(message)
        assert (
            routes_page.driver.find_element(
                *routes_page.message_for_driver_input
            ).get_property("value")
            == message
        )

    #### blankets and napkins
    def test_blanket_and_napkins(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_taxi_button()
        routes_page.click_button_comfort()

        routes_page.select_blanket_and_napkins()
        element = routes_page.driver.find_element(
            *routes_page.blanket_and_napkins_switch
        )
        assert element.is_selected() or element.get_attribute("aria-checked") == "true"

    ### Order 2 ice creams
    def test_add_two_ice_creams(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_taxi_button()
        routes_page.click_button_comfort()

        routes_page.add_two_ice_creams()
        assert routes_page.get_ice_cream_count() == "2"

    #### Taxi order
    def test_search_taxi_modal(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_taxi_button()
        routes_page.click_button_comfort()

        routes_page.driver.find_element(*routes_page.final_order_button).click()

        modal = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(routes_page.order_search)
        )

        assert modal is not None

    #### Driver assignment
    def test_driver_assignment(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_taxi_button()
        routes_page.click_button_comfort()

        routes_page.driver.find_element(*routes_page.final_order_button).click()

        assigned = routes_page.wait_for_driver_assignment()

        assert assigned is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
