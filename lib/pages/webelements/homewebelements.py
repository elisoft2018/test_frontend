from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.CSS_SELECTOR, '.title-wrapper h2.title.dark')
    signin_button = (By.CSS_SELECTOR, '.menu__wrapper .menu-label__wrapper button')
    search_button = (By.XPATH, '//button[@aria-label="Buscar"]')
    origin_flight_input = (By.CSS_SELECTOR, '.pM26-mod-multi-value .NhpT[aria-label="Origen"]')
    destination_flight_input = (By.CSS_SELECTOR, '.zEiP-formBody .NhpT[aria-label="Destino"]')
    start_date_input = (By.XPATH, '//div[@aria-label="Fecha de inicio"]')
    end_date_input = (By.XPATH, '//div[@aria-label="Fecha de fin"]')
    select_option = (By.XPATH, '//div[contains(@class,"item-title") and text()='']')
