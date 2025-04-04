import socket
import os
import time

def send_file(file_path, host='127.0.0.1', port=12346):
    try:
        # Создаем сокет и подключаемся к серверу
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        # Отправляем имя файла
        file_name = os.path.basename(file_path)
        client_socket.send(file_name.encode('utf-8'))
        print(f"Отправлено имя файла: {file_name}")

        # Открываем файл и начинаем передачу данных
        with open(file_path, "rb") as file:
            while True:
                bytes_read = file.read(1024)
                if not bytes_read:
                    break
                client_socket.send(bytes_read)
                time.sleep(0.01)  # Задержка для избежания перегрузки сети

        print(f"Файл {file_name} успешно отправлен.")
    except Exception as e:
        print(f"Ошибка при отправке файла: {e}")
    finally:
        client_socket.close()

# Пример использования функции send_file
if __name__ == '__main__':
    send_file("example.txt", host="127.0.0.1", port=12346)
