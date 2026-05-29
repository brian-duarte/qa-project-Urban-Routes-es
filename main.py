import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from LOCATORS import UrbanRoutesLocators
from selenium.webdriver.support import expected_conditions as EC


# no modificar (código de retrieve_phone_code)
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación.
    """

    import json
    import time
    from selenium.common import WebDriverException

    code = None
    for i in range(10):
        try:
            logs = [
                log["message"]
                for log in driver.get_log("performance")
                if log.get("message") and "api/v1/number?number" in log.get("message")
            ]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd(
                    "Network.getResponseBody",
                    {"requestId": message_data["params"]["requestId"]},
                )
                code = "".join([x for x in body["body"] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception(
                "No se encontró el código de confirmación del teléfono.\n"
                "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación."
            )
        return code


class UrbanRoutesPage:
    def __init__(self, driver):
        # LOCALIZADORES DESDE, HASTA, TAXI Y COMFORT
        self.driver = driver
        self.from_field = UrbanRoutesLocators.address_from
        self.to_field = UrbanRoutesLocators.address_to
        self.taxi_button = UrbanRoutesLocators.taxi_button
        self.comfort_button = UrbanRoutesLocators.button_comfort
        # LOCALIZADORES DE TELEFONO
        self.phone_entry_button = UrbanRoutesLocators.phone_number
        self.phone_input_field = UrbanRoutesLocators.phone_number_field
        self.phone_next_button = UrbanRoutesLocators.phone_number_siguiente
        self.sms_code_field = UrbanRoutesLocators.code_sms
        self.sms_confirm_button = UrbanRoutesLocators.confirm_sms
        # LOCALIZADORES METODO DE PAGO
        self.payment_method_button = UrbanRoutesLocators.payment_method_button
        self.add_card_button = UrbanRoutesLocators.add_payment_card
        self.card_number_input = UrbanRoutesLocators.payment_card_input
        self.card_code_input = UrbanRoutesLocators.card_code_input
        self.card_click_away_element = UrbanRoutesLocators.click_away_payment
        self.card_save_button = UrbanRoutesLocators.save_card_button
        # LOCALIZADORES MENSAJE PARA EL CONDUCTOR
        self.message_for_driver_input = UrbanRoutesLocators.message_for_driver_input
        self.blanket_and_napkins_switch = UrbanRoutesLocators.blanket_and_napkins
        self.ice_cream_button = UrbanRoutesLocators.ice_cream
        # PEDIR TAXI
        self.final_order_button = UrbanRoutesLocators.final_order_taxi
        # LOCALIZADOR OPCIONAL
        self.order_search = UrbanRoutesLocators.search_taxi
        self.driver_arrival = UrbanRoutesLocators.driver_arrival_taxi

    ##METODOS DE RUTA

    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.from_field)
        )

        field = self.driver.find_element(*self.from_field)
        field.clear()
        field.send_keys(from_address)
        field.send_keys(Keys.RETURN)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.to_field)
        )

        field = self.driver.find_element(*self.to_field)
        field.clear()
        field.send_keys(to_address)
        field.send_keys(Keys.RETURN)

    def set_route(self, from_address, to_address):
        """Combina la configuración de las direcciones de inicio y fin."""
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property("value")

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property("value")

    def click_taxi_button(self):

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.taxi_button)
        )

        button = self.driver.find_element(*self.taxi_button)
        button.click()

    def click_button_comfort(self):

        # Importación local para claridad

        # 1. Esperar la PRESENCIA del elemento en el DOM (más indulgente que visibility)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.comfort_button)
        ).click()

    def button_comfort_selected(self):
        ###Verifica si la opción Comfort está seleccionada, basándose en la clase 'active'
        comfort_element = self.driver.find_element(*self.comfort_button)
        return "active" in comfort_element.get_attribute("class")

    ##METODO DE TELEFONO Y SMS

    def set_phone_number(self, phone_number):
        ###Abre el modal, ingresa número y presiona 'Siguiente'
        self.driver.find_element(*self.phone_entry_button).click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.phone_input_field)
        ).send_keys(phone_number)

        self.driver.find_element(*self.phone_next_button).click()

    def enter_sms_code(self):
        ###Obtiene el SMS de los logs y lo ingresa
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.sms_code_field)
        )

        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.sms_code_field).send_keys(code)

        self.driver.find_element(*self.sms_confirm_button).click()

    ##METODO DE PAGO

    def click_payment_method_button(self):
        ##Abre el modal pago
        self.driver.find_element(*self.payment_method_button).click()

    def add_new_card(self):
        ##Hacer clic en 'Agregar tarjeta' dentro del modal de pago
        self.driver.find_element(*self.add_card_button).click()

    def set_card_details(self, card_number, card_code):
        # Ingresa el número de tarjeta y el código CVV.
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.card_number_input)
        )

        # Ingresar número de tarjeta
        card_number_element = self.driver.find_element(*self.card_number_input)
        card_number_element.send_keys(card_number)

        # Ingresar código CVV/CVC
        card_code_element = self.driver.find_element(*self.card_code_input)
        card_code_element.send_keys(card_code)

        # Hacer clic fuera de los campos para que se valide la entrada (usando el localizador click_away_payment)
        self.driver.find_element(*self.card_click_away_element).click()

    def save_card(self):
        """Guarda la tarjeta agregada haciendo clic en el botón 'Agregar'."""
        self.driver.find_element(*self.card_save_button).click()

    ## MENSAJE PARA EL CONDUCTOR

    def set_message_for_driver(self, message):
        ##Ingresa un mensaje en el campo 'Traiga un aperitivo'
        self.driver.find_element(*self.message_for_driver_input).send_keys(message)

    def select_blanket_and_napkins(self):
        ####Activa el switch de 'Manta y pañuelos'
        self.driver.find_element(*self.blanket_and_napkins_switch).click()

    def add_two_ice_creams(self):
        ####Hace clic dos veces en el botón '+' para añadir 2 helados
        plus_button = self.driver.find_element(*self.ice_cream_button)
        plus_button.click()
        plus_button.click()

    def get_ice_cream_count(self):
        ##Devuelve el valor actual del contador de helados."""
        element = self.driver.find_element(*UrbanRoutesLocators.ice_cream_value)
        return element.text.strip()

    def wait_for_driver_assignment(self, timeout=40):
        try:
            wait = WebDriverWait(self.driver, timeout)

            # 1. Esperar a que el texto CAMBIE (ya no diga "Buscar automóvil")
            wait.until(
                expected_conditions.not_text_to_be_present_in_element(
                    self.order_search, "Buscar automóvil"
                )
            )

            # 2. Esperar a que aparezca la tarjeta del conductor
            wait.until(
                expected_conditions.visibility_of_element_located(self.driver_arrival)
            )
            return True
        except Exception:
            return False
