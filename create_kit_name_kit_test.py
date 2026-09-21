import sender_stand_request
import data

# Вспомогательная функция для подстановки значения в поле name
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Вспомогательная функция для позитивных проверок (Код 201)
def positive_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    
    assert response.status_code == 201
    assert response.json()["name"] == name

# Вспомогательная функция для негативных проверок с передачей name (Код 400)
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    
    assert response.status_code == 400

# Вспомогательная функция для теста №10 (когда поле name отсутствует)
def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    
    assert response.status_code == 400

# --- 11 ТЕСТОВ ИЗ ЧЕК-ЛИСТА ---

# Тест 1. Допустимое количество символов (1)
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

# Тест 2. Допустимое количество символов (511)
def test_create_kit_511_letter_in_name_get_success_response():
    name_511 = "a" * 511
    positive_assert(name_511)

# Тест 3. Количество символов меньше допустимого (0)
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400("")

# Тест 4. Количество символов больше допустимого (512)
def test_create_kit_512_letter_in_name_get_error_response():
    name_512 = "a" * 512
    negative_assert_code_400(name_512)

# Тест 5. Разрешены английские буквы
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Разрешены русские буквы
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Разрешены спецсимволы
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert('"№%@"')

# Тест 8. Разрешены пробелы
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(" Человек и КО ")

# Тест 9. Разрешены цифры
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")

# Тест 10. Параметр не передан в запросе
def test_create_kit_no_name_get_error_response():
    kit_body = {}
    negative_assert_no_name(kit_body)

# Тест 11. Передан другой тип параметра (число)
def test_create_kit_number_type_name_get_error_response():
    negative_assert_code_400(123)