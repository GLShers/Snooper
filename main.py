import requests

def search_vk_by_phone(phone_number, access_token):
    url = 'https://api.vk.com/method/users.search'
    params = {
        'q': phone_number,
        'access_token': access_token,
        'v': '5.131'  # Версия API
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'response' in data:
        return data['response']
    else:
        return None

# Пример использования
if __name__ == "__main__":
    phone = '89210060271'
    token = 'cf6ac10fcf6ac10fcf6ac10fa2cc71aaceccf6acf6ac10fa9d208b6c6c7ac8d23b98dd0'
    result = search_vk_by_phone(phone, token)
    print(result)