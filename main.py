import requests

def validate_phone_number(api_key, phone_number):
    # URL для проверки номера
    url = f"https://api.numlookupapi.com/v1/validate/{phone_number}?apikey={api_key}"
    
    # Выполнение GET-запроса
    response = requests.get(url)
    
    # Проверка статуса ответа
    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except requests.exceptions.JSONDecodeError:
            return {"error": "Failed to decode JSON response"}
    else:
        return {"error": f"Request failed with status code {response.status_code}, response text: {response.text}"}

# Ваш API-ключ
api_key = "num_live_HQWbCfNDhO42LEBZNKe3vIpfPE5FgNfaD489DHfT"

# Номер телефона для проверки
phone_number = "+7"+input("Input number +7")

# Вызов функции и вывод результата
result = validate_phone_number(api_key, phone_number)
print("Номер телефона:" , result['number'], "\nСтрана:", result['country_name'], "\nЛокация:", result['location'],
       "\nОператор сотовой связи:",result['carrier'])
