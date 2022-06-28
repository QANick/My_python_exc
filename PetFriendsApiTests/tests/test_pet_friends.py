from api import PetFriends
from settings import valid_email, valid_password
from settings import valid_name, valid_animal_type, valid_age
from settings import valid_filter
import os

pf = PetFriends ()

def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    # Тест на получение auth_key с валидными email and password
     status, result = pf.get_api_key(email, password)
     assert status == 200
    # проверка на получение корректного ответа от сервера
     assert 'key' in result
    #проверка на наличие ключа в ответе от сервера


def test_get_all_pets_with_valid_key(filter = ''):
    # Тест на получение списка питомцев с использованием корректного auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # получаем auth_key через соответствующий get-запрос
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    # проверка на получение корректного ответа от сервера
    assert len(result['pets']) > 0
    # проверка на наличие питомцев в ответе от сервера по данному запросу

def test_post_create_pet_simple_valid_date(name = valid_name, animal_type = valid_animal_type, age = valid_age):
    # Тест на добавление питомца без фото с использованием корректных данных name, animal_type, age
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # получаем auth_key через соответствующий get-запрос
    status, result = pf.post_create_pet_simple(auth_key, name, animal_type, age)
    _, get_pets = pf.get_list_of_pets(auth_key, valid_filter)
    assert status == 200
    # проверка на получение корректного ответа от сервера
    assert result ['id'] == get_pets ['pets'][0]['id']
    # проверка на наличие добавленного питомца в списке питомцев

def test_post_create_pet_with_photo_valid_date(name = valid_name, animal_type = valid_animal_type, age = valid_age, pet_photo=os.path.join('images', 'cat.jpeg')):
    # Тест на добавление питомца (с фото) с использованием корректных данных name, animal_type, age, pet_photo
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # получаем auth_key через соответствующий get-запрос
    status, result = pf.post_create_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    # проверка на получение корректного ответа от сервера
    assert result['name'] == name
    # проверка на соответствие имени добавляемого питомца с добавленным через запрос

def test_post_set_photo_for_pet_valid_data(pet_photo=os.path.join('images', 'cat_new.jpeg')):
    # Тест на добавление фото питомца
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # получаем auth_key через соответствующий get-запрос
    _, my_pets = pf.get_list_of_pets(auth_key, valid_filter)
    # получаем список питомцев в переменной my_pets через соответствующий get-запрос
    if len(my_pets['pets']) > 0:
        pet_id = my_pets['pets'][0]['id']
        # сохраняем значнеие id питомца в переменную pet_id
        old_pet_photo = my_pets['pets'][0]['pet_photo']
        # сохраняем старое фото в переменную old_pet_photo
        status, result = pf.post_set_photo_for_pet(auth_key, pet_id, pet_photo)
        assert status == 200
        # проверка на получение корректного ответа от сервера
        assert result['pet_photo'] != old_pet_photo
        # проверка на фактическое изменение параметра 'pet_photo'
        _, my_pets = pf.get_list_of_pets(auth_key, valid_filter)
        # снова получаем обновленный список питомцев в переменной my_pets через соответствующий get-запрос
        assert result['pet_photo'] == my_pets['pets'][0]['pet_photo']
        # проверка на соотвествие добавляемой фото с фактически добавленной через запрос
    else:
        print('There is no my pets')

def test_put_successful_update_pet_info (name='Sam', animal_type='Kiti', age='4'):
    # Тест на обновление информации о питомца с корректными данными
   _, auth_key = pf.get_api_key(valid_email, valid_password)
    # получаем auth_key через соответствующий get-запрос
   _, my_pets = pf.get_list_of_pets(auth_key, valid_filter)
    # получаем список питомцев в переменной my_pets через соответствующий get-запрос
   if len(my_pets['pets']) > 0:
       status, result = pf.put_update_info_about_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
       assert status == 200
       # проверка на получение корректного ответа от сервера
       assert result['name'] == name
       # проверка на корреткность обновлённых данных
   else:
       raise Exception("There is no my pets")

def test_delete_successful_last_added_pet ():
    # Тест на удаление последнего питомца из списка my_pets
   _, auth_key = pf.get_api_key(valid_email, valid_password)
    # получаем auth_key через соответствующий get-запрос
   _, my_pets = pf.get_list_of_pets(auth_key, valid_filter)
    # получаем список питомцев в переменной my_pets через соответствующий get-запрос
   if len(my_pets['pets']) > 0:
       last_pet_pet_id = my_pets['pets'][0]['id']
       #сохраняем id питомца, которого будем удалять
       status, result = pf.delete_last_added_pet(auth_key, my_pets['pets'][0]['id'])
       assert status == 200
       # проверка на получение корректного ответа от сервера
       _, my_pets = pf.get_list_of_pets(auth_key, valid_filter)
       assert my_pets['pets'][0]['id'] != last_pet_pet_id
       # проверка на успешное удаление последнего питомца из списка своих питомцев
   else:
       raise Exception("There is no my pets")

#Список негативных тестов:
def test_get_api_key_with_empty_email(email='', password=valid_password):
    # Тест на получение auth_key с использованием пустого значения email
    status, result = pf.get_api_key(email, password)
    assert status == 200
    # ожидаем 200, получаем 403
    assert 'key' in result

def test_get_api_key_with_incorrect_password(email=valid_email, password='incorrect'):
    # Тест на получение auth_key с использованием некорректного значения password
    status, result = pf.get_api_key(email, password)
    assert status == 200
    # ожидаем 200, получаем 403
    assert 'key' in result

def test_get_all_pets_with_incorrect_auth_key(filter = ''):
    # Тест на получение списка питомцев с ипользованием некорректного значения auth_key
    auth_key = {'key': 'dfgdgfbdggfdgdfj3e3'}
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    # ожидаем 200, получаем 403
    assert len(result['pets']) > 0

def test_get_all_pets_with_incorrect_value_of_filter(filter = 'pets'):
    # Тест на получение списка питомцев с ипользованием некорректного значения filter
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    # ожидаем 200, получаем 403
    assert len(result['pets']) > 0

def test_delete_last_added_pet_with_incorrect_pet_id():
    # Тест на удаление последнего питомца из списка my_pets c использованием некооретного id питомца
   _, auth_key = pf.get_api_key(valid_email, valid_password)
   _, my_pets = pf.get_list_of_pets(auth_key, valid_filter)
   if len(my_pets['pets']) > 0:
       last_pet_pet_id = my_pets['pets'][0]['id']
       status, result = pf.delete_last_added_pet(auth_key, pet_id='dsgfhdsfgh')
       assert status == 200
       _, my_pets = pf.get_list_of_pets(auth_key, valid_filter)
       assert my_pets['pets'][0]['id'] != last_pet_pet_id
       #ожидаем, что питомец будет удалён и id из запроса на удаление не будет совпадать с id полследнего
       #питомца в списке my_pets.  По факту получаем равенство, тест провален.
   else:
       raise Exception("There is no my pets")

def test_post_create_pet_with_nonexistent_photo(name = valid_name, animal_type = valid_animal_type, age = valid_age, pet_photo=os.path.join('images', 'cat222.jpeg')):
    # Тест на добавление питомца с несуществующим фото
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_create_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    #тест провален, так как уканного фото не найдено

def test_post_create_pet_with_text_file_instead_of_image(name = valid_name, animal_type = valid_animal_type, age = valid_age, pet_photo=os.path.join('images', 'text.txt')):
    # Тест на добавление питомца с текстовым файлом вместо графического в качестве фото
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_create_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    #ожидаем 400, а получаем 200. Питомец добавляется на сайт без фото
    assert result['name'] == name

def test_put_update_pet_info_with_incorrect_petid(name='Sam', animal_type='Kiti', age='4'):
    # Тест на обновление информации о питомце с указанием некорректного id
   _, auth_key = pf.get_api_key(valid_email, valid_password)
   _, my_pets = pf.get_list_of_pets(auth_key, valid_filter)
   if len(my_pets['pets']) > 0:
       status, result = pf.put_update_info_about_pet(auth_key, my_pets['pets'][0]['name'], name, animal_type, age)
       #указываем некорректный pet_id
       assert status == 200
       # ожидаем 200, получаем 400
       assert result['name'] == name
   else:
       raise Exception("There is no my pets")

