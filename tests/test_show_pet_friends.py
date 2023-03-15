import pytest
from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_show_pet_friends():
    pytest.driver.implicitly_wait(10)
    # Вводим email
    pytest.driver.find_element(By.ID, "email").send_keys('sawfish72@gmail.com')
    # Вводим пароль
    pytest.driver.find_element(By.ID, "pass").send_keys('irina2301')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    images = pytest.driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-text')
    assert names[0].text != ''
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ',' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0