from operator import contains

from selenium.webdriver.common.by import By


class UrbanRoutesLocators:
    # LOCALIZADORES DESDE, HASTA, TAXI Y COMFORT
    address_from = (By.ID, "from")
    address_to = (By.ID, "to")
    taxi_button = (By.CSS_SELECTOR, ".button.round")
    button_comfort = (By.XPATH, "//div[text()='Comfort' and @class='tcard-title']")
    # LOCALIZADORES DE TELEFONO
    phone_number = (By.CSS_SELECTOR, "div.np-button")
    phone_number_field = (By.ID, "phone")
    phone_number_siguiente = (By.XPATH, "//button[contains(text(), 'Siguiente')]")
    code_sms = (By.CSS_SELECTOR, "div.input-container input#code")
    confirm_sms = (By.XPATH, "//button[normalize-space()='Confirmar']")
    # LOCALIZADORES METODO DE PAGO
    payment_method_button = (By.CSS_SELECTOR, "div.pp-button.filled")
    add_payment_card = (By.CSS_SELECTOR, "div.pp-plus-container")
    payment_card_input = (By.CSS_SELECTOR, "div.card-number-input")
    card_code_input = (By.CSS_SELECTOR, "div.card-code-input")
    click_away_payment = (By.CSS_SELECTOR, "div.card-wrapper")
    save_card_button = (By.XPATH, "//button[normalize-space()='Agregar']")
    # LOCALIZADORES MENSAJE PARA EL CONDUCTOR
    message_for_driver_input = (By.XPATH, "//input[@placeholder='Traiga un aperitivo']")
    blanket_and_napkins = (
        By.XPATH,
        "//div[contains(text(),'Manta y pañuelos')]/following-sibling::div[@class='r-sw']",
    )
    ice_cream = (
        By.XPATH,
        "//div[contains(text(), 'Helado')]/following-sibling::div//div[@class='counter-plus']",
    )
    ice_cream_value = (
        By.XPATH,
        "//div[contains(text(), 'Helado')]/following-sibling::div//div[@class='counter-value']",
    )
    # PEDIR TAXI
    final_order_taxi = (By.CSS_SELECTOR, "div[class*='smart-button-wrapper']")
    # BUSQUEDA DE AUTOMOVIL
    search_taxi = (
        By.XPATH,
        "//div[@class='order-header-title' and contains(text(), 'Buscar automóvil')]",
    )
    driver_arrival_taxi = (
        By.XPATH,
        "//div[@class='order-header-content']//div[@class='order-header-title']",
    )
