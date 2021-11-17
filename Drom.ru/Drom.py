import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import HtmlTestRunner


def switch(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.number_of_windows_to_be(2))
    original_window = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break


def check(driver, button, xpath, title):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        assert title in driver.title
        assert driver.find_element(By.XPATH, xpath)
        print(f"The page for {button} profile is correct")
        driver.close()
    except:
        driver.quit()
        raise Exception(f"Error with {button} profile")


def moveTo(driver):
    moreMenu = driver.find_element(By.XPATH, '//div[contains(text(), "Еще")]')
    webdriver.ActionChains(driver).move_to_element(moreMenu).perform()


def buttonClick(driver, button, xpath, title):
    driver.find_element(By.XPATH, xpath).click()
    assert title in driver.title
    print(f'The "{button}" button is clickable')


def selectRegion(driver, region, city):
    driver.find_element(By.XPATH, '//a[@href="https://www.drom.ru/my_region/"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, f'//a[@href="https://www.drom.ru/my_region/?set_region={region}"]').click()
    numOfGoods = driver.find_elements(By.XPATH, f'//span[@data-ftid = "bull_location"][contains(text(), {city})]')
    print(f"There are {len(numOfGoods)} announcements from {city}, 20 announcements expected")
    assert len(numOfGoods) == 20


class Chrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("D:\webdriver\chromedriver.exe")

    def test_searchPanel_chrome(self):
        driver_chrome = self.driver
        driver_chrome.maximize_window()
        driver_chrome.get("https://auto.drom.ru/")
        assert driver_chrome.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_chrome.title
        print("\"Продажа автомобилей в России\" for searchPanel test (Chrome) in title")
        print(f"The title is \"{driver_chrome.title}\"")
        driver_chrome.find_element(By.XPATH, "//*[@placeholder=\"Марка\"]").click()
        driver_chrome.find_element(By.XPATH, "//div[contains(text(), \"Toyota\")]").click()
        time.sleep(0.5)
        driver_chrome.find_element(By.XPATH, "//*[@placeholder=\"Модель\"]").click()
        driver_chrome.find_element(By.XPATH, "//div[contains(text(), \"Camry\")]").click()
        time.sleep(0.5)
        driver_chrome.find_element(By.XPATH, "//Button[contains(text(), \"Поколение\")]").click()
        driver_chrome.find_element(By.XPATH, "//div[contains(text(), \"9 поколение (XV70)\")]").click()
        time.sleep(0.5)
        driver_chrome.find_element(By.XPATH, "//*[@placeholder=\"Цена от, руб.\"]").click()
        driver_chrome.find_element(By.XPATH, "//*[@placeholder=\"Цена от, руб.\"]").send_keys("3000000")
        time.sleep(0.5)
        driver_chrome.find_element(By.XPATH, "//Button[contains(text(), \"Объем от, л\")]").click()
        driver_chrome.find_element(By.XPATH, "//div[contains(text(), \"3.0\")]").click()
        time.sleep(0.5)
        driver_chrome.find_element(By.XPATH, "//Button[contains(text(), \"Год от\")]").click()
        driver_chrome.find_element(By.XPATH, "(//div[text()='2020'])[1]").click()
        time.sleep(0.5)
        driver_chrome.find_element(By.XPATH, "//Button[contains(text(), \"КПП\")]").click()
        driver_chrome.find_element(By.XPATH, "//div[contains(text(), \"Автомат\")]").click()
        time.sleep(0.5)
        driver_chrome.find_element(By.XPATH, "//Button[contains(text(), \"Топливо\")]").click()
        driver_chrome.find_element(By.XPATH, "//div[contains(text(), \"Бензин\")]").click()
        time.sleep(0.5)
        driver_chrome.find_element(By.XPATH, "//div[contains(text(), \"Показать\")]").click()
        time.sleep(1)
        numOfGoods = driver_chrome.find_elements(By.XPATH,
                                                 "//*[@data-ftid=\"bull_title\"][contains(text(), \"Toyota Camry\")]")
        print(f"There are {len(numOfGoods)} goods with name \"Toyota Camry\". Expected result is 20")
        assert len(numOfGoods) == 20
        driver_chrome.quit()

    def test_socialButtons_chrome_1280x1024(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1280, 1024)
        driver_chrome.get("https://auto.drom.ru/")
        original_window = driver_chrome.current_window_handle
        assert driver_chrome.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_chrome.title
        print("\"Продажа автомобилей в России\" for socialButtons test (Chrome) in title")
        print(f"The title is \"{driver_chrome.title}\"")
        assert driver_chrome.find_element(By.XPATH, "//a[@title=\"Instagram Дрома\"]")
        print("The page contains Instagram button")
        driver_chrome.find_element(By.XPATH, "//a[@title=\"Instagram Дрома\"]").click()
        switch(driver_chrome)
        check(driver_chrome, "Instagram", "//h2[contains(text(), \"drom\")]", "Дром")
        driver_chrome.switch_to.window(original_window)
        assert driver_chrome.find_element(By.XPATH, "//a[@title=\"Дром ВКонтакте\"]")
        print("The page contains VK button")
        driver_chrome.find_element(By.XPATH, "//a[@title=\"Дром ВКонтакте\"]").click()
        switch(driver_chrome)
        check(driver_chrome, "VK", "//h1[contains(text(), \"Дром\")]", "ВКонтакте")
        driver_chrome.switch_to.window(original_window)
        assert driver_chrome.find_element(By.XPATH, "//a[@title=\"Канал Дрома на YouTube\"]")
        print("The page contains YouTube button")
        driver_chrome.find_element(By.XPATH, "//a[@title=\"Канал Дрома на YouTube\"]").click()
        switch(driver_chrome)
        check(driver_chrome, "YouTube", "//*[@id=\"text\"][contains(text(), \"Дром\")]", "YouTube")
        driver_chrome.switch_to.window(original_window)
        assert driver_chrome.find_element(By.XPATH, "//a[@title=\"Twitter Дрома\"]")
        print("The page contains Twitter button")
        driver_chrome.find_element(By.XPATH, "//a[@title=\"Twitter Дрома\"]").click()
        switch(driver_chrome)
        check(driver_chrome, "Twitter", "(//span[contains(.,'Дром')])[5]", "Твиттер")
        driver_chrome.switch_to.window(original_window)
        assert driver_chrome.find_element(By.XPATH, "//a[@title=\"Телеграм Дрома\"]")
        print("The page contains Telegram button")
        driver_chrome.find_element(By.XPATH, "//a[@title=\"Телеграм Дрома\"]").click()
        switch(driver_chrome)
        check(driver_chrome, "Telegram", "//span[contains(text(), \"Дром\")]", "Telegram")
        driver_chrome.switch_to.window(original_window)
        assert driver_chrome.find_element(By.XPATH, "//a[@title=\"Дром на Одноклассниках\"]")
        print("The page contains OK button")
        driver_chrome.find_element(By.XPATH, "//a[@title=\"Дром на Одноклассниках\"]").click()
        switch(driver_chrome)
        check(driver_chrome, "OK", "//h1[contains(text(), \"Дром\")]", "OK")
        driver_chrome.switch_to.window(original_window)
        assert driver_chrome.find_element(By.XPATH, "//a[@title=\"Дром в Фейсбук\"]")
        print("The page contains Facebook button")
        driver_chrome.find_element(By.XPATH, "//a[@title=\"Дром в Фейсбук\"]").click()
        switch(driver_chrome)
        check(driver_chrome, "Facebook", "(//span[contains(text(), \"Дром\")])[1]", "Facebook")
        driver_chrome.switch_to.window(original_window)
        assert driver_chrome.find_element(By.XPATH, "//a[@title=\"TikTok Дрома\"]")
        print("The page contains TikTok button")
        driver_chrome.find_element(By.XPATH, "//a[@title=\"TikTok Дрома\"]").click()
        switch(driver_chrome)
        check(driver_chrome, "TikTok", "//h2[contains(text(), \"drom\")]", "TikTok")
        driver_chrome.quit()

    def test_mainMenu_chrome(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1920, 1280)
        driver_chrome.get("https://auto.drom.ru/")
        assert driver_chrome.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_chrome.title
        print("\"Продажа автомобилей в России\" for main menu test (Chrome) in title")
        print(f"The title is \"{driver_chrome.title}\"")
        buttonClick(driver_chrome, "Автомобили",
                    "(//a[contains(text(), \"Автомобили\")])[1]", "Продажа автомобилей в России")
        buttonClick(driver_chrome, "Спецтехника",
                    '//*[@href="https://spec.drom.ru/?utm_term=drom-spec-equip-experiment"]', "Спецтехника и грузовики")
        buttonClick(driver_chrome, "Запчасти", "(//a[contains(text(), \"Запчасти\")])[1]", "Запчасти, шины, диски")
        buttonClick(driver_chrome, "Отзывы", "(//a[contains(text(), \"Отзывы\")])[1]", "Отзывы автовладельцев")
        buttonClick(driver_chrome, "Каталог", "(//a[contains(text(), \"Каталог\")])[1]", "Каталог автомобилей")
        buttonClick(driver_chrome, "Шины", '(//a[@href="https://baza.drom.ru/wheel/tire/"])[1]', "Купить шины")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Электромобили",
                    '//*[@href="https://www.drom.ru/electro/"]', "Электромобили в России")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Дром ОСАГО",
                    '//*[@data-ga-stats-name="topmenu_osago"]', "DROM OSAGO")
        driver_chrome.back()
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Проверка по VIN", '//*[text()="Проверка по VIN"]', "Проверка авто по VIN")
        driver_chrome.back()
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Оценить авто", '//*[@href="https://auto.drom.ru/rate_car/"]', "Оценить авто")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Форумы", '//*[@href="https://forums.drom.ru/"]', "Форумы об автомобилях в России")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "ПДД онлайн", '//*[@href="https://www.drom.ru/pdd/"]', "ПДД 2021")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Вопросы и ответы",
                    '//*[@href="https://www.drom.ru/faq/"]', "Вопросы и Ответы по автомобилям")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Рейтинг авто", '//*[@href="https://www.drom.ru/topcars/"]', "Рейтинг автомобилей")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Каталог шин", '//*[@href="https://www.drom.ru/shina/"]', "Каталог шин")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Видеорегистраторы",
                    '//*[@href="https://videoregistrator.drom.ru/"]', "Видеорегистраторы")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Статьи", '//*[@href="https://www.drom.ru/info/"]', "Тест-драйвы и статьи")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Автопутешествия", '//*[@href="https://travel.drom.ru/"]', "Автопутешествия")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Автоспорт", '//*[@href="https://www.drom.ru/info/autosport/"]', "Автоспорт")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Правовые вопросы", '//*[@href="https://law.drom.ru/"]', "Правовые вопросы")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Карта сайта", '//*[@href="https://www.drom.ru/sitemap/"]', "Карта сайта")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Реклама на дроме",
                    '//*[@href="https://www.drom.ru/commerce/"]', "Размещение рекламы на Дроме")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Разместить прайс",
                    '//*[@href="https://baza.drom.ru/for-business"]', "Автомобильные объявления")
        moveTo(driver_chrome)
        buttonClick(driver_chrome, "Помощь",
                    '//*[@href="https://my.drom.ru/help/VozniklaProblemanaDrome"]', "Возникла проблема на Дроме")
        driver_chrome.quit()

    def test_regionSelect_chrome(self):
        driver_chrome = self.driver
        driver_chrome.maximize_window()
        driver_chrome.get("https://auto.drom.ru/")
        assert driver_chrome.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_chrome.title
        print("\"Продажа автомобилей в России\" for region select test (Chrome) in title")
        print(f"The title is \"{driver_chrome.title}\"")
        selectRegion(driver_chrome, 54, "Novosibirsk")
        selectRegion(driver_chrome, 77, "Moscow")
        driver_chrome.quit()

    def test_techniqueSelect_chrome(self):
        driver_chrome = self.driver
        driver_chrome.maximize_window()
        driver_chrome.get("https://auto.drom.ru/")
        assert driver_chrome.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_chrome.title
        print("\"Продажа автомобилей в России\" for technique select test (Chrome) in title")
        print(f"The title is \"{driver_chrome.title}\"")
        driver_chrome.find_element(By.XPATH, '(//a[@href="https://spec.drom.ru/"])[1]').click()
        assert "Спецтехника и грузовики" in driver_chrome.title
        assert "Спецтехника и грузовики" in driver_chrome.find_element(By.CLASS_NAME, 'js-viewdir-subject').text
        print('The "Спецтехника" button is correct')
        driver_chrome.back()
        driver_chrome.find_element(By.XPATH, '(//a[@href="https://baza.drom.ru/"])[1]').click()
        assert "Запчасти, шины, диски" in driver_chrome.title
        assert "запчасти, товары и услуги для авто" in driver_chrome.find_element(By.CLASS_NAME,
                                                                                  'js-viewdir-subject').text
        print('The "Запчасти, шины, сервис" button is correct')
        driver_chrome.back()
        driver_chrome.find_element(By.XPATH, '(//a[@href="https://water.drom.ru/"])[1]').click()
        assert "Водная техника" in driver_chrome.title
        assert "Водная техника" in driver_chrome.find_element(By.CLASS_NAME, 'js-viewdir-subject').text
        print('The "Водная техника" button is correct')
        driver_chrome.back()
        driver_chrome.find_element(By.XPATH, '(//a[@href="https://moto.drom.ru/"])[1]').click()
        assert "Продажа и покупка мототехники" in driver_chrome.title
        assert "Продажа и покупка мототехники" in driver_chrome.find_element(By.CLASS_NAME, 'js-viewdir-subject').text
        print('The "Мототехника" button is correct')
        driver_chrome.quit()


class Firefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_searchPanel_firefox(self):
        driver_firefox = self.driver
        driver_firefox.maximize_window()
        driver_firefox.get("https://auto.drom.ru/")
        assert driver_firefox.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_firefox.title
        print("\"Продажа автомобилей в России\" for searchPanel test (Firefox) in title")
        print(f"The title is \"{driver_firefox.title}\"")
        driver_firefox.find_element(By.XPATH, "//*[@placeholder=\"Марка\"]").click()
        driver_firefox.find_element(By.XPATH, "//div[contains(text(), \"Toyota\")]").click()
        time.sleep(0.5)
        driver_firefox.find_element(By.XPATH, "//*[@placeholder=\"Модель\"]").click()
        driver_firefox.find_element(By.XPATH, "//div[contains(text(), \"Camry\")]").click()
        time.sleep(0.5)
        driver_firefox.find_element(By.XPATH, "//Button[contains(text(), \"Поколение\")]").click()
        driver_firefox.find_element(By.XPATH, "//div[contains(text(), \"9 поколение (XV70)\")]").click()
        time.sleep(0.5)
        driver_firefox.find_element(By.XPATH, "//*[@placeholder=\"Цена от, руб.\"]").click()
        driver_firefox.find_element(By.XPATH, "//*[@placeholder=\"Цена от, руб.\"]").send_keys("3000000")
        time.sleep(0.5)
        driver_firefox.find_element(By.XPATH, "//Button[contains(text(), \"Объем от, л\")]").click()
        driver_firefox.find_element(By.XPATH, "//div[contains(text(), \"3.0\")]").click()
        time.sleep(0.5)
        driver_firefox.find_element(By.XPATH, "//Button[contains(text(), \"Год от\")]").click()
        driver_firefox.find_element(By.XPATH, "(//div[text()='2020'])[1]").click()
        time.sleep(0.5)
        driver_firefox.find_element(By.XPATH, "//Button[contains(text(), \"КПП\")]").click()
        driver_firefox.find_element(By.XPATH, "//div[contains(text(), \"Автомат\")]").click()
        time.sleep(0.5)
        driver_firefox.find_element(By.XPATH, "//Button[contains(text(), \"Топливо\")]").click()
        driver_firefox.find_element(By.XPATH, "//div[contains(text(), \"Бензин\")]").click()
        time.sleep(0.5)
        driver_firefox.find_element(By.XPATH, "//div[contains(text(), \"Показать\")]").click()
        time.sleep(1)
        numOfGoods = driver_firefox.find_elements(By.XPATH,
                                                  "//*[@data-ftid=\"bull_title\"][contains(text(), \"Toyota Camry\")]")
        print(f"There are {len(numOfGoods)} goods with name \"Toyota Camry\". Expected result is 20")
        assert len(numOfGoods) == 20
        driver_firefox.quit()

    def test_socialButtons_firefox_1280x1024(self):
        driver_firefox = self.driver
        driver_firefox.set_window_size(1280, 1024)
        driver_firefox.get("https://auto.drom.ru/")
        original_window = driver_firefox.current_window_handle
        assert driver_firefox.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_firefox.title
        print("\"Продажа автомобилей в России\" for socialButtons test (Firefox) in title")
        print(f"The title is \"{driver_firefox.title}\"")
        assert driver_firefox.find_element(By.XPATH, "//a[@title=\"Instagram Дрома\"]")
        print("The page contains Instagram button")
        driver_firefox.find_element(By.XPATH, "//a[@title=\"Instagram Дрома\"]").click()
        switch(driver_firefox)
        check(driver_firefox, "Instagram", "//h2[contains(text(), \"drom\")]", "Дром")
        driver_firefox.switch_to.window(original_window)
        assert driver_firefox.find_element(By.XPATH, "//a[@title=\"TikTok Дрома\"]")
        print("The page contains TikTok button")
        driver_firefox.find_element(By.XPATH, "//a[@title=\"TikTok Дрома\"]").click()
        switch(driver_firefox)
        check(driver_firefox, "TikTok", "//h2[contains(text(), \"drom\")]", "TikTok")
        driver_firefox.switch_to.window(original_window)
        assert driver_firefox.find_element(By.XPATH, "//a[@title=\"Дром ВКонтакте\"]")
        print("The page contains VK button")
        driver_firefox.find_element(By.XPATH, "//a[@title=\"Дром ВКонтакте\"]").click()
        switch(driver_firefox)
        check(driver_firefox, "VK", "//h1[contains(text(), \"Дром\")]", "ВКонтакте")
        driver_firefox.switch_to.window(original_window)
        assert driver_firefox.find_element(By.XPATH, "//a[@title=\"Канал Дрома на YouTube\"]")
        print("The page contains YouTube button")
        driver_firefox.find_element(By.XPATH, "//a[@title=\"Канал Дрома на YouTube\"]").click()
        switch(driver_firefox)
        check(driver_firefox, "YouTube", "//*[@id=\"text\"][contains(text(), \"Дром\")]", "YouTube")
        driver_firefox.switch_to.window(original_window)
        assert driver_firefox.find_element(By.XPATH, "//a[@title=\"Twitter Дрома\"]")
        print("The page contains Twitter button")
        driver_firefox.find_element(By.XPATH, "//a[@title=\"Twitter Дрома\"]").click()
        switch(driver_firefox)
        check(driver_firefox, "Twitter", "(//span[contains(.,'Дром')])[5]", "Твиттер")
        driver_firefox.switch_to.window(original_window)
        assert driver_firefox.find_element(By.XPATH, "//a[@title=\"Телеграм Дрома\"]")
        print("The page contains Telegram button")
        driver_firefox.find_element(By.XPATH, "//a[@title=\"Телеграм Дрома\"]").click()
        switch(driver_firefox)
        check(driver_firefox, "Telegram", "//span[contains(text(), \"Дром\")]", "Telegram")
        driver_firefox.switch_to.window(original_window)
        assert driver_firefox.find_element(By.XPATH, "//a[@title=\"Дром на Одноклассниках\"]")
        print("The page contains OK button")
        driver_firefox.find_element(By.XPATH, "//a[@title=\"Дром на Одноклассниках\"]").click()
        switch(driver_firefox)
        check(driver_firefox, "OK", "//h1[contains(text(), \"Дром\")]", "OK")
        driver_firefox.switch_to.window(original_window)
        assert driver_firefox.find_element(By.XPATH, "//a[@title=\"Дром в Фейсбук\"]")
        print("The page contains Facebook button")
        driver_firefox.find_element(By.XPATH, "//a[@title=\"Дром в Фейсбук\"]").click()
        switch(driver_firefox)
        check(driver_firefox, "Facebook", "(//span[contains(text(), \"Дром\")])[1]", "Facebook")
        driver_firefox.quit()

    def test_mainMenu_firefox(self):
        driver_firefox = self.driver
        driver_firefox.set_window_size(1920, 1280)
        driver_firefox.get("https://auto.drom.ru/")
        assert driver_firefox.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_firefox.title
        print("\"Продажа автомобилей в России\" for main menu test (Firefox) in title")
        print(f"The title is \"{driver_firefox.title}\"")
        buttonClick(driver_firefox, "Автомобили",
                    "(//a[contains(text(), \"Автомобили\")])[1]", "Продажа автомобилей в России")
        buttonClick(driver_firefox, "Спецтехника",
                    '//*[@href="https://spec.drom.ru/?utm_term=drom-spec-equip-experiment"]', "Спецтехника и грузовики")
        buttonClick(driver_firefox, "Запчасти", "(//a[contains(text(), \"Запчасти\")])[1]", "Запчасти, шины, диски")
        buttonClick(driver_firefox, "Отзывы", "(//a[contains(text(), \"Отзывы\")])[1]", "Отзывы автовладельцев")
        buttonClick(driver_firefox, "Каталог", "(//a[contains(text(), \"Каталог\")])[1]", "Каталог автомобилей")
        buttonClick(driver_firefox, "Шины", '(//a[@href="https://baza.drom.ru/wheel/tire/"])[1]', "Купить шины")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Электромобили",
                    '//*[@href="https://www.drom.ru/electro/"]', "Электромобили в России")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Дром ОСАГО",
                    '//*[@data-ga-stats-name="topmenu_osago"]', "DROM OSAGO")
        driver_firefox.back()
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Проверка по VIN", '//*[text()="Проверка по VIN"]', "Проверка авто по VIN")
        driver_firefox.back()
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Оценить авто", '//*[@href="https://auto.drom.ru/rate_car/"]', "Оценить авто")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Форумы", '//*[@href="https://forums.drom.ru/"]', "Форумы об автомобилях в России")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "ПДД онлайн", '//*[@href="https://www.drom.ru/pdd/"]', "ПДД 2021")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Вопросы и ответы",
                    '//*[@href="https://www.drom.ru/faq/"]', "Вопросы и Ответы по автомобилям")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Рейтинг авто", '//*[@href="https://www.drom.ru/topcars/"]', "Рейтинг автомобилей")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Каталог шин", '//*[@href="https://www.drom.ru/shina/"]', "Каталог шин")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Видеорегистраторы",
                    '//*[@href="https://videoregistrator.drom.ru/"]', "Видеорегистраторы")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Статьи", '//*[@href="https://www.drom.ru/info/"]', "Тест-драйвы и статьи")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Автопутешествия", '//*[@href="https://travel.drom.ru/"]', "Автопутешествия")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Автоспорт", '//*[@href="https://www.drom.ru/info/autosport/"]', "Автоспорт")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Правовые вопросы", '//*[@href="https://law.drom.ru/"]', "Правовые вопросы")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Карта сайта", '//*[@href="https://www.drom.ru/sitemap/"]', "Карта сайта")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Реклама на дроме",
                    '//*[@href="https://www.drom.ru/commerce/"]', "Размещение рекламы на Дроме")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Разместить прайс",
                    '//*[@href="https://baza.drom.ru/for-business"]', "Автомобильные объявления")
        moveTo(driver_firefox)
        buttonClick(driver_firefox, "Помощь",
                    '//*[@href="https://my.drom.ru/help/VozniklaProblemanaDrome"]', "Возникла проблема на Дроме")
        driver_firefox.quit()

    def test_regionSelect_firefox(self):
        driver_firefox = self.driver
        driver_firefox.maximize_window()
        driver_firefox.get("https://auto.drom.ru/")
        assert driver_firefox.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_firefox.title
        print("\"Продажа автомобилей в России\" for region select test (Firefox) in title")
        print(f"The title is \"{driver_firefox.title}\"")
        selectRegion(driver_firefox, 54, "Novosibirsk")
        selectRegion(driver_firefox, 77, "Moscow")
        driver_firefox.quit()

    def test_techniqueSelect_firefox(self):
        driver_firefox = self.driver
        driver_firefox.maximize_window()
        driver_firefox.get("https://auto.drom.ru/")
        assert driver_firefox.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_firefox.title
        print("\"Продажа автомобилей в России\" for technique select test (Firefox) in title")
        print(f"The title is \"{driver_firefox.title}\"")
        driver_firefox.find_element(By.XPATH, '(//a[@href="https://spec.drom.ru/"])[1]').click()
        assert "Спецтехника и грузовики" in driver_firefox.title
        assert "Спецтехника и грузовики" in driver_firefox.find_element(By.CLASS_NAME, 'js-viewdir-subject').text
        print('The "Спецтехника" button is correct')
        driver_firefox.back()
        driver_firefox.find_element(By.XPATH, '(//a[@href="https://baza.drom.ru/"])[1]').click()
        assert "Запчасти, шины, диски" in driver_firefox.title
        assert "запчасти, товары и услуги для авто" in driver_firefox.find_element(By.CLASS_NAME,
                                                                                   'js-viewdir-subject').text
        print('The "Запчасти, шины, сервис" button is correct')
        driver_firefox.back()
        driver_firefox.find_element(By.XPATH, '(//a[@href="https://water.drom.ru/"])[1]').click()
        assert "Водная техника" in driver_firefox.title
        assert "Водная техника" in driver_firefox.find_element(By.CLASS_NAME, 'js-viewdir-subject').text
        print('The "Водная техника" button is correct')
        driver_firefox.back()
        driver_firefox.find_element(By.XPATH, '(//a[@href="https://moto.drom.ru/"])[1]').click()
        assert "Продажа и покупка мототехники" in driver_firefox.title
        assert "Продажа и покупка мототехники" in driver_firefox.find_element(By.CLASS_NAME, 'js-viewdir-subject').text
        print('The "Мототехника" button is correct')
        driver_firefox.quit()


class Edge(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_searchPanel_edge(self):
        driver_edge = self.driver
        driver_edge.maximize_window()
        driver_edge.get("https://auto.drom.ru/")
        assert driver_edge.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_edge.title
        print("\"Продажа автомобилей в России\" for searchPanel test (Edge) in title")
        print(f"The title is \"{driver_edge.title}\"")
        driver_edge.find_element(By.XPATH, "//*[@placeholder=\"Марка\"]").click()
        driver_edge.find_element(By.XPATH, "//div[contains(text(), \"Toyota\")]").click()
        time.sleep(0.5)
        driver_edge.find_element(By.XPATH, "//*[@placeholder=\"Модель\"]").click()
        driver_edge.find_element(By.XPATH, "//div[contains(text(), \"Camry\")]").click()
        time.sleep(0.5)
        driver_edge.find_element(By.XPATH, "//Button[contains(text(), \"Поколение\")]").click()
        driver_edge.find_element(By.XPATH, "//div[contains(text(), \"9 поколение (XV70)\")]").click()
        time.sleep(0.5)
        driver_edge.find_element(By.XPATH, "//*[@placeholder=\"Цена от, руб.\"]").click()
        driver_edge.find_element(By.XPATH, "//*[@placeholder=\"Цена от, руб.\"]").send_keys("3000000")
        time.sleep(0.5)
        driver_edge.find_element(By.XPATH, "//Button[contains(text(), \"Объем от, л\")]").click()
        driver_edge.find_element(By.XPATH, "//div[contains(text(), \"3.0\")]").click()
        time.sleep(0.5)
        driver_edge.find_element(By.XPATH, "//Button[contains(text(), \"Год от\")]").click()
        driver_edge.find_element(By.XPATH, "(//div[text()='2020'])[1]").click()
        time.sleep(0.5)
        driver_edge.find_element(By.XPATH, "//Button[contains(text(), \"КПП\")]").click()
        driver_edge.find_element(By.XPATH, "//div[contains(text(), \"Автомат\")]").click()
        time.sleep(0.5)
        driver_edge.find_element(By.XPATH, "//Button[contains(text(), \"Топливо\")]").click()
        driver_edge.find_element(By.XPATH, "//div[contains(text(), \"Бензин\")]").click()
        time.sleep(0.5)
        driver_edge.find_element(By.XPATH, "//div[contains(text(), \"Показать\")]").click()
        time.sleep(1)
        numOfGoods = driver_edge.find_elements(By.XPATH,
                                                 "//*[@data-ftid=\"bull_title\"][contains(text(), \"Toyota Camry\")]")
        print(f"There are {len(numOfGoods)} goods with name \"Toyota Camry\". Expected result is 20")
        assert len(numOfGoods) == 20
        driver_edge.quit()

    def test_socialButtons_edge_1280x1024(self):
        driver_edge = self.driver
        driver_edge.set_window_size(1280, 1024)
        driver_edge.get("https://auto.drom.ru/")
        original_window = driver_edge.current_window_handle
        assert driver_edge.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_edge.title
        print("\"Продажа автомобилей в России\" for socialButtons test (Edge) in title")
        print(f"The title is \"{driver_edge.title}\"")
        assert driver_edge.find_element(By.XPATH, "//a[@title=\"Instagram Дрома\"]")
        print("The page contains Instagram button")
        driver_edge.find_element(By.XPATH, "//a[@title=\"Instagram Дрома\"]").click()
        switch(driver_edge)
        check(driver_edge, "Instagram", "//h2[contains(text(), \"drom\")]", "Дром")
        driver_edge.switch_to.window(original_window)
        assert driver_edge.find_element(By.XPATH, "//a[@title=\"Дром ВКонтакте\"]")
        print("The page contains VK button")
        driver_edge.find_element(By.XPATH, "//a[@title=\"Дром ВКонтакте\"]").click()
        switch(driver_edge)
        check(driver_edge, "VK", "//h1[contains(text(), \"Дром\")]", "ВКонтакте")
        driver_edge.switch_to.window(original_window)
        assert driver_edge.find_element(By.XPATH, "//a[@title=\"Канал Дрома на YouTube\"]")
        print("The page contains YouTube button")
        driver_edge.find_element(By.XPATH, "//a[@title=\"Канал Дрома на YouTube\"]").click()
        switch(driver_edge)
        check(driver_edge, "YouTube", "//*[@id=\"text\"][contains(text(), \"Дром\")]", "YouTube")
        driver_edge.switch_to.window(original_window)
        assert driver_edge.find_element(By.XPATH, "//a[@title=\"Twitter Дрома\"]")
        print("The page contains Twitter button")
        driver_edge.find_element(By.XPATH, "//a[@title=\"Twitter Дрома\"]").click()
        switch(driver_edge)
        check(driver_edge, "Twitter", "(//span[contains(.,'Дром')])[5]", "Твиттер")
        driver_edge.switch_to.window(original_window)
        assert driver_edge.find_element(By.XPATH, "//a[@title=\"Телеграм Дрома\"]")
        print("The page contains Telegram button")
        driver_edge.find_element(By.XPATH, "//a[@title=\"Телеграм Дрома\"]").click()
        switch(driver_edge)
        check(driver_edge, "Telegram", "//span[contains(text(), \"Дром\")]", "Telegram")
        driver_edge.switch_to.window(original_window)
        assert driver_edge.find_element(By.XPATH, "//a[@title=\"Дром на Одноклассниках\"]")
        print("The page contains OK button")
        driver_edge.find_element(By.XPATH, "//a[@title=\"Дром на Одноклассниках\"]").click()
        switch(driver_edge)
        check(driver_edge, "OK", "//h1[contains(text(), \"Дром\")]", "OK")
        driver_edge.switch_to.window(original_window)
        assert driver_edge.find_element(By.XPATH, "//a[@title=\"Дром в Фейсбук\"]")
        print("The page contains Facebook button")
        driver_edge.find_element(By.XPATH, "//a[@title=\"Дром в Фейсбук\"]").click()
        switch(driver_edge)
        check(driver_edge, "Facebook", "(//span[contains(text(), \"Дром\")])[1]", "Facebook")
        driver_edge.switch_to.window(original_window)
        assert driver_edge.find_element(By.XPATH, "//a[@title=\"TikTok Дрома\"]")
        print("The page contains TikTok button")
        driver_edge.find_element(By.XPATH, "//a[@title=\"TikTok Дрома\"]").click()
        switch(driver_edge)
        check(driver_edge, "TikTok", "//h2[contains(text(), \"drom\")]", "TikTok")
        driver_edge.quit()

    def test_mainMenu_edge(self):
        driver_edge = self.driver
        driver_edge.set_window_size(1920, 1280)
        driver_edge.get("https://auto.drom.ru/")
        assert driver_edge.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_edge.title
        print("\"Продажа автомобилей в России\" for main menu test (Edge) in title")
        print(f"The title is \"{driver_edge.title}\"")
        buttonClick(driver_edge, "Автомобили",
                    "(//a[contains(text(), \"Автомобили\")])[1]", "Продажа автомобилей в России")
        buttonClick(driver_edge, "Спецтехника",
                    '//*[@href="https://spec.drom.ru/?utm_term=drom-spec-equip-experiment"]', "Спецтехника и грузовики")
        buttonClick(driver_edge, "Запчасти", "(//a[contains(text(), \"Запчасти\")])[1]", "Запчасти, шины, диски")
        buttonClick(driver_edge, "Отзывы", "(//a[contains(text(), \"Отзывы\")])[1]", "Отзывы автовладельцев")
        buttonClick(driver_edge, "Каталог", "(//a[contains(text(), \"Каталог\")])[1]", "Каталог автомобилей")
        buttonClick(driver_edge, "Шины", '(//a[@href="https://baza.drom.ru/wheel/tire/"])[1]', "Купить шины")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Электромобили",
                    '//*[@href="https://www.drom.ru/electro/"]', "Электромобили в России")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Дром ОСАГО",
                    '//*[@data-ga-stats-name="topmenu_osago"]', "DROM OSAGO")
        driver_edge.back()
        moveTo(driver_edge)
        buttonClick(driver_edge, "Проверка по VIN", '//*[text()="Проверка по VIN"]', "Проверка авто по VIN")
        driver_edge.back()
        moveTo(driver_edge)
        buttonClick(driver_edge, "Оценить авто", '//*[@href="https://auto.drom.ru/rate_car/"]', "Оценить авто")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Форумы", '//*[@href="https://forums.drom.ru/"]', "Форумы об автомобилях в России")
        moveTo(driver_edge)
        buttonClick(driver_edge, "ПДД онлайн", '//*[@href="https://www.drom.ru/pdd/"]', "ПДД 2021")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Вопросы и ответы",
                    '//*[@href="https://www.drom.ru/faq/"]', "Вопросы и Ответы по автомобилям")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Рейтинг авто", '//*[@href="https://www.drom.ru/topcars/"]', "Рейтинг автомобилей")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Каталог шин", '//*[@href="https://www.drom.ru/shina/"]', "Каталог шин")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Видеорегистраторы",
                    '//*[@href="https://videoregistrator.drom.ru/"]', "Видеорегистраторы")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Статьи", '//*[@href="https://www.drom.ru/info/"]', "Тест-драйвы и статьи")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Автопутешествия", '//*[@href="https://travel.drom.ru/"]', "Автопутешествия")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Автоспорт", '//*[@href="https://www.drom.ru/info/autosport/"]', "Автоспорт")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Правовые вопросы", '//*[@href="https://law.drom.ru/"]', "Правовые вопросы")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Карта сайта", '//*[@href="https://www.drom.ru/sitemap/"]', "Карта сайта")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Реклама на дроме",
                    '//*[@href="https://www.drom.ru/commerce/"]', "Размещение рекламы на Дроме")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Разместить прайс",
                    '//*[@href="https://baza.drom.ru/for-business"]', "Автомобильные объявления")
        moveTo(driver_edge)
        buttonClick(driver_edge, "Помощь",
                    '//*[@href="https://my.drom.ru/help/VozniklaProblemanaDrome"]', "Возникла проблема на Дроме")
        driver_edge.quit()

    def test_regionSelect_edge(self):
        driver_edge = self.driver
        driver_edge.maximize_window()
        driver_edge.get("https://auto.drom.ru/")
        assert driver_edge.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_edge.title
        print("\"Продажа автомобилей в России\" for region select test (Edge) in title")
        print(f"The title is \"{driver_edge.title}\"")
        selectRegion(driver_edge, 54, "Novosibirsk")
        selectRegion(driver_edge, 77, "Moscow")
        driver_edge.quit()

    def test_techniqueSelect_edge(self):
        driver_edge = self.driver
        driver_edge.maximize_window()
        driver_edge.get("https://auto.drom.ru/")
        assert driver_edge.find_element(By.XPATH, "//*[@fill=\"#DB001B\"]")
        assert "Продажа автомобилей в России" in driver_edge.title
        print("\"Продажа автомобилей в России\" for technique select test (Edge) in title")
        print(f"The title is \"{driver_edge.title}\"")
        driver_edge.find_element(By.XPATH, '(//a[@href="https://spec.drom.ru/"])[1]').click()
        assert "Спецтехника и грузовики" in driver_edge.title
        assert "Спецтехника и грузовики" in driver_edge.find_element(By.CLASS_NAME, 'js-viewdir-subject').text
        print('The "Спецтехника" button is correct')
        driver_edge.back()
        driver_edge.find_element(By.XPATH, '(//a[@href="https://baza.drom.ru/"])[1]').click()
        assert "Запчасти, шины, диски" in driver_edge.title
        assert "запчасти, товары и услуги для авто" in driver_edge.find_element(By.CLASS_NAME,
                                                                                  'js-viewdir-subject').text
        print('The "Запчасти, шины, сервис" button is correct')
        driver_edge.back()
        driver_edge.find_element(By.XPATH, '(//a[@href="https://water.drom.ru/"])[1]').click()
        assert "Водная техника" in driver_edge.title
        assert "Водная техника" in driver_edge.find_element(By.CLASS_NAME, 'js-viewdir-subject').text
        print('The "Водная техника" button is correct')
        driver_edge.back()
        driver_edge.find_element(By.XPATH, '(//a[@href="https://moto.drom.ru/"])[1]').click()
        assert "Продажа и покупка мототехники" in driver_edge.title
        assert "Продажа и покупка мототехники" in driver_edge.find_element(By.CLASS_NAME, 'js-viewdir-subject').text
        print('The "Мототехника" button is correct')
        driver_edge.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../HtmlReports'))
