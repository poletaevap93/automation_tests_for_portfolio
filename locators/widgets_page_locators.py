from selenium.webdriver.common.by import By


class AccordianPageLocators:

    SECTION_FIRST = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECTION_CONTENT_FIRST = (By.CSS_SELECTOR, "div[id='section1Content'] p")

    SECTION_SECOND = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECTION_CONTENT_SECOND = (By.CSS_SELECTOR, "div[id='section2Content'] p")

    SECTION_THIRD = (By.CSS_SELECTOR, "div[id='section3Heading']")
    SECTION_CONTENT_THIRD = (By.CSS_SELECTOR, "div[id='section3Content'] p")

class AutoCompletePageLocators: # тестирование форм, куда можно забивать цвета, в один инпут вставляется одно название, в другой можно несколько

    MULTI_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTI_VALUE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value']")  # локатор значений, которые вбиты в инпуте
    MULTI_VALUE_DELETE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")

    SINGLE_VALUE = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")
    SINGLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")
