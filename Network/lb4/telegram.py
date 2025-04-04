import requests


def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': message
    }
    try:
        response = requests.post(url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке сообщения в Telegram: {e}")
        return None


# Пример отправки уведомления
def send_interface_down_notification(status):
    bot_token = "7667116612:AAGuKO8RVUOBoXECGRAWaBcHOeONyyWGS-U"
    chat_id = "90600942"

    if status is None or int(status) != 1:  # 1 означает "up"
        message = "Сбой интерфейса на устройстве 192.168.1.1!"
        result = send_telegram_message(bot_token, chat_id, message)
        if result:
            print("Уведомление отправлено успешно!")
        else:
            print("Не удалось отправить уведомление!")

# Пример вызова (предполагается, что переменная 'status' уже определена)
# status = snmp_get('192.168.1.1', '1.3.6.1.2.1.2.2.1.8.1')  # Раскомментируйте, если используете SNMP
# send_interface_down_notification(status)
