from selenium.webdriver.common.by import By


class CommonElement:
    elements = [{'select_option': '//div[contains(@class,"item-title") and text()="{}"]'}]


def get_element_by_value(key, type_selector, replace_value):
    web_element = None
    for element in CommonElement.elements:
        if key in element:
            if type_selector=='XPATH':
                web_element = (By.XPATH, element[key].format(replace_value))
            elif type_selector=='ID':
                web_element = (By.ID, element[key].format(replace_value))
            elif type_selector=='CSS_SELECTOR':
                web_element = (By.CSS_SELECTOR, element[key].format(replace_value))
            else:
                print("unknown selector type")
            """match type_selector:
                case 'XPATH':
                    web_element = (By.XPATH, element[key].format(replace_value))
                case 'ID':
                    web_element = (By.ID, element[key].format(replace_value))
                case 'CSS':
                    web_element = (By.CSS_SELECTOR, element[key].format(replace_value))
                case _:
                    print("unknown type selector")
                    """
    return web_element

