import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json

class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru'

    def get_api_key(self, email: str, password: str) -> json:
        """Метод делает запрос к API сервера, возвращает статус запроса и результат в формате json
        c уникальным ключом пользователя, найденным по валидным email и password """
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'/api/key', headers = headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key: json, filter: str) -> json:
        '''Метод делает запрос к API сервера, возвращает статус запроса и результат в формате json
        cо списком всех питомцев, при условии что параметр "filter" пустой'''
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'/api/pets', headers = headers, params=filter)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_create_pet_simple(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        '''Метод делает запрос к API сервера, возвращает статус запроса и результат в формате json
        с информацией о питомце с указанными name, animal_type, age'''
        headers = {'auth_key': auth_key['key']}
        data = {'name': name, 'animal_type': animal_type, 'age': age}

        res = requests.post(self.base_url+'/api/create_pet_simple', headers = headers, data=data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_create_pet_with_photo(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo) -> json:
        '''Метод делает запрос к API сервера, возвращает статус запроса и результат в формате json
                с информацией о питомце с указанными name, animal_type, age, pet_photo'''
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url+'/api/pets', headers = headers, data=data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_set_photo_for_pet(self, auth_key: json, pet_id: json, pet_photo) -> json:
        '''Метод делает запрос к API сервера, возвращает статус запроса и результат в формате json
                с информацией о питомце с указанными name, animal_type, age и добавленном pet_photo'''
        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url+'/api/pets/set_photo/' + pet_id, headers = headers, data=data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def put_update_info_about_pet(self, auth_key: json, pet_id: json, name: str, animal_type: str, age: str) -> json:
        '''Метод делает запрос к API сервера, возвращает статус запроса и результат в формате json
                с обновленной валидной информацией о питомце'''
        headers = {'auth_key': auth_key['key']}
        data = {'name': name, 'animal_type': animal_type, 'age': age}

        res = requests.put(self.base_url+'/api/pets/' + pet_id, headers = headers, data=data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_last_added_pet(self, auth_key: json, pet_id: json) -> json:
        '''Метод делает запрос к API сервера, возвращает статус запроса и результат в формате json
            без питомца, id которого был удалён'''
        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url+'/api/pets/' + pet_id, headers = headers,)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


