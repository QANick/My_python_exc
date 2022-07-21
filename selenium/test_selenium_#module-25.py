import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('/Users/nick/chromedriver')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   time.sleep(3)

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('lulmajistu@vusra.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12Jw?!')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Нажимаем на кнопку "Мои питомцы" на главной странице "PetFriends"
   WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/my_pets"]'))).click()
   # Сохраняем в переменную row_count количество строк таблицы питомцев
   row_count = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody tr')))
   # Сохраняем в переменную amount_pets текст из элемента с атрибутом класса ".col-sm-4 left"
   amount_pets = pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]').text
   intlist = []
   # Получаем из переменной amount_pets список подстрок, разделённых пробелом и проходим циклом по этому списку,
   # добавляя в переменную intlist только целые числа
   for t in amount_pets.split():
      try:
         intlist.append(int(t))
      except ValueError:
         pass
   # Проверяем что первый элемент списка intlist, соответствующий количеству питомцев, равен количеству строк
   # в таблице питомцев
   assert intlist[0] == len(row_count) #Тест проходит без ошибок и при добалении нового питомца не падает


def test_show_that_pets_with_images_more_half():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('lulmajistu@vusra.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12Jw?!')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   pytest.driver.find_element_by_xpath('//a[@href="/my_pets"]').click()
   # Сохраняем в переменную row_count количество строк таблицы питомцев
   row_count = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody tr')))
   print(len(row_count))
   # Сохраняем в переменную images все фотографии питомцев
   images = WebDriverWait(pytest.driver, 10).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, 'th[scope="row"] img')))
   count = 0
   # Проходим циклом по всем фото в images и проверяем наличии атрибута src.
   # При наличии непустого src увеличиваем счётчик count на 1
   for i in range(len(images)):
      if images[i].get_attribute('src') != "":
         count=count+1
      else:
         count=count
   # Проверяем, что больше чем у половины питомцев есть фото
   assert (int(len(row_count)/2))<count, "Питомцев с фото меньше половины"
   #Тест падает, так как из 63 питомцев (половина это 31) фото есть только у 18


def test_show_that_all_pets_have_name_age_animal_type():
   pytest.driver.implicitly_wait(10)
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('lulmajistu@vusra.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12Jw?!')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   pytest.driver.find_element_by_xpath('//a[@href="/my_pets"]').click()
   # Сохраняем в переменную amount_td количество элементов с тэгом 'td' (имя+возраст+порода)
   amount_td = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//tbody/tr/td')))
   list=[]
   # Сохраняем в список list текст всех элементов с тэгом td (имена+возраст+порода)
   for i in range (len(amount_td)):
      txt=pytest.driver.find_elements_by_xpath('//tbody/tr/td')[i].text
      list.append(txt)
   # Проверяем, что cписок не содержит нулевых значений
   for i in range(len(list)):
      assert list[i] != '', 'Есть питомцы либо без имени, либо без породы, либо без возраста'
      #Тест падает так как в таблице есть питомцы либо без имени, либо без породы, либо бех возраста

def test_show_that_all_pets_have_different_names():
   pytest.driver.implicitly_wait(10)
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('lulmajistu@vusra.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12Jw?!')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   pytest.driver.find_element_by_xpath('//a[@href="/my_pets"]').click()
   # Сохраняем в переменную amount_td количество элементов с тэгом 'td' (имя+возраст+порода)
   amount_td = pytest.driver.find_elements_by_xpath('//tbody/tr/td')
   list=[]
   # Сохраняем в список list текст всех элементов с тэгом td
   for i in range (len(amount_td)):
      txt=pytest.driver.find_elements_by_xpath('//tbody/tr/td')[i].text
      list.append(txt)
   # Берем из списка элементы с шагом 4, соответствующие именам питомцев, и сохраняем в переменную names
   names=list[::4]
   # Преобразуем список names в множество set_names
   set_names=set(names)
   # Проверяем, что длина списка равна длине множества
   assert len(names) == len(set_names), "Есть одинаковые имена питомцев"
   #Тест падает, так как имена питомцев повторяются и множество set_names
   # содержит меньше элементов, чем список names

def test_show_that_all_pets_have_different_names_animal_type_age():
   pytest.driver.implicitly_wait(10)
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('lulmajistu@vusra.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12Jw?!')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   pytest.driver.find_element_by_xpath('//a[@href="/my_pets"]').click()
   # Сохраняем в переменную row_count количество строк таблицы питомцев
   row_count = pytest.driver.find_elements_by_xpath('//tbody/tr')
   list = []
   # Сохраняем в список list текст из каждой строки таблицы питомцев
   for i in range(len(row_count)):
      txt = pytest.driver.find_elements_by_xpath('//tbody/tr')[i].text
      list.append(txt)
   # Преобразуем список list в множество set_list
   set_list = set(list)
   # Проверяем, что длина списка равна длине множества (проверка, что каждый элемент списка уникален)
   assert len(list) == len(set_list), "Есть полностью одинаковые питомцы"
   #Тест падает, так как в списке есть повторяющиеся питомцы





