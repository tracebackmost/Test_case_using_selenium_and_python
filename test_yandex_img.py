from YandexPage import MainPage


def test_yandex_img(browser):
    # Заходим на сайт yandex.ru
    yandex_main_page = MainPage(browser)
    yandex_main_page.go_to_site()
    # Проверяем что ссылка "Картинки" присутствует на странице
    yandex_main_page.img_url()
    # Кликаем по ссылке
    yandex_main_page.click_on_the_img_button()
    # Проверяем,что перешли на url https://yandex.ru/images/,
    # Открываем 1 категорию, проверяем что она открылась, в поиске верный текст
    yandex_main_page.open_the_category_and_check()
    # Открываем 1 картинку, проверяем что открылась
    yandex_main_page.open_the_first_picture_and_check()
    # Нажимаем кнопку "вперед" на картинке
    yandex_main_page.click_to_button_forward()
    # Нажимаем кнопку "назад" на картинке, картинка меняется на предыдущую
    yandex_main_page.click_to_button_back()
    # Проверяем, что это та же картинка
    yandex_main_page.compare_pictures()
