from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_YANDEX_SEARCH_RESULT = (By.CSS_SELECTOR, "#search-result > .serp-item a.link > b")
    LOCATOR_YANDEX_IMG = (By.LINK_TEXT, "Картинки")
    LOCATOR_YANDEX_MODAL_WINDOW = (By.CLASS_NAME, "Modal-Content")


class MainPage(BasePage):

    # Поиск в Яндексе

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        time.sleep(5)
        assert search_field != None, "Поле поиска не найдено"
        return search_field

    def suggest(self):
        suggest = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_SUGGEST, time=5)
        assert suggest != None, "Таблица подсказок не найдена"
        return suggest

    def click_on_the_search_button(self):
        self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=5).click()
        result = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_RESULT, time=5)
        assert result != None, "По вашему запросу ничего не найдено"
        return

    def search_result(self):
        result = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_RESULT, time=5)
        items = [elem.text.strip() for elem in result[:5]]
        assert "tensor.ru" in items, "По вашему запросу ничего не найдено"
        return

    # Картинки на Яндексе

    def img_url(self):
        images = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_IMG, time=5)
        assert images != None, "Раздел 'Картинки' не найден"
        return images

    def click_on_the_img_button(self):
        self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_IMG, time=5).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return

    def open_the_category_and_check(self):
        url_of_the_page = self.driver.current_url
        assert "https://yandex.ru/images/" in url_of_the_page, "Ссылка не совпадает"
        img_category = self.driver.find_elements_by_class_name("PopularRequestList-Shadow")
        img_category[0].click()
        img_category_text = self.driver.find_elements_by_class_name("PopularRequestList-SearchText")
        img_category_text_value = img_category_text[0].text
        time.sleep(3)
        search_field_text = self.driver.find_elements_by_class_name("input__control")
        search_field_text_value = search_field_text[0].get_attribute("value")
        assert search_field_text_value in img_category_text_value, "Открыта не верная категория"
        return

    def open_the_first_picture_and_check(self):
        first_picture = self.driver.find_elements_by_class_name("serp-item__link")
        first_picture[0].click()
        time.sleep(5)
        modal_window = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_MODAL_WINDOW, time=5)
        assert modal_window != None, "Картинка не открылась"
        return first_picture

    def click_to_button_forward(self):
        ActionChains(self.driver).key_down(Keys.RIGHT).perform()
        time.sleep(3)
        return

    def click_to_button_back(self):
        ActionChains(self.driver).key_down(Keys.LEFT).perform()
        time.sleep(3)
        return

    def compare_pictures(self):
        img_list = self.driver.find_elements_by_class_name("MMGallery-ItemImageOverlay")
        assert img_list[0] != img_list[1], "Картинки не совпадают"
        return

