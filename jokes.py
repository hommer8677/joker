import requests, random
from bs4 import BeautifulSoup as BS 

url="https://vse-shutochki.ru/anekdoty"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def getJoke() -> str:
    res = list()
    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            soup = BS(response.text, 'lxml')
            jokes = soup.find_all('p')
            
            for p in jokes:
                text = p.get_text(strip=True)

                if not text: continue
                if "Самые смешные" in text or "Добро пожаловать" in text: continue
                
                formatted_text = text.replace(" -", "\n-").replace(" —", "\n—")
                
                res.append(formatted_text)
        else: 
            print(f"Ошибка сервера. Статус-код: {response.status_code}")

    except requests.exceptions.ConnectionError as e:
        print("Сайт всё ещё блокирует соединение. Возможно, ваш IP попал во временный бан.")
        print(f"Детали ошибки: {e}")
        return "-1"
    return random.choice(res) if len(res) > 0 else "-1"
