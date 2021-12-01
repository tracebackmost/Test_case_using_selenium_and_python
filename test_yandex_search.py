from YandexPage import MainPage


def test_yandex_search(browser):
    # Заходим на сайт yandex.ru
    yandex_main_page = MainPage(browser)
    yandex_main_page.go_to_site()
    # Проверяем наличие поля поиска и вводим в поисковую строку "Тензор"
    yandex_main_page.enter_word("Тензор")
    # Проверяем, что появилась таблица с подсказками
    yandex_main_page.suggest()
    # Нажатимаем Enter и проверяем, что появляется таблица результатов поиска
    yandex_main_page.click_on_the_search_button()
    # Проверяем, что в первых 5 результатах есть ссылка на tensor.ru
    yandex_main_page.search_result()


