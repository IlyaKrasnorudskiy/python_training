import socket
import threading

def handle_client(client_socket, addr):
    print(f"Подключен клиент: {addr}")
    try:
        # Получение данных от клиента
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Получено сообщение от {addr}: {data}")

        # Отправка ответа клиенту
        client_socket.send("Сообщение получено".encode('utf-8'))
    except Exception as e:
        print(f"Ошибка при обработке клиента {addr}: {e}")
    finally:
        client_socket.close()
        print(f"Соединение с {addr} закрыто.")

def start_server(host='0.0.0.0', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер запущен на {host}:{port} и ожидает подключения...")

    while True:
        # Принимаем подключение клиента
        client_socket, addr = server_socket.accept()

        # Создаем поток для обработки клиента
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == '__main__':
    start_server()