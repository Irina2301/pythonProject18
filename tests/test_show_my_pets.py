import pytest
from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_show_my_pets():
   pytest.driver.implicitly_wait(10)
   # Вводим email
   pytest.driver.find_element(By.ID, "email").send_keys('valid_email')
   # Вводим пароль
   pytest.driver.find_element(By.ID, "pass").send_keys('valid_password')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME,'h1').text == "PetFriends"

