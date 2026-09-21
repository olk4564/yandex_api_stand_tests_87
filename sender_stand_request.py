# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

import requests

import data

def post_new_user(body):
    return requests.post (
        configuration.URL_SERVICE +
configuration.CREATE_USER_PATH,
    json=body,
    headers=data.headers
    )

def get_new_user_token():
    response_user = post_new_user(data.user_body)
    auth_token = response_user.json()["authToken"]
    return auth_token

def post_new_client_kit(kit_body):
    auth_token = get_new_user_token()
    current_headers = data.headers.copy()
    current_headers["Authorization"] = f"Bearer {auth_token}"

    response_kit = requests.post(
        configuration.URL_SERVICE +
        configuration.KITS_PATH,
        json=kit_body,
        headers=current_headers
    )

    return response_kit

if __name__ == "__main__":
    response = post_new_client_kit(data.kit_body)
    print("Статус ответа:", response.status_code)
    print("Тело ответа:", response.json())