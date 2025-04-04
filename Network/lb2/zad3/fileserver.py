import socket
import threading

def handle_file_transfer(client_socket, addr):
    print(f"Подключен клиент для передачи файла: {addr}")
    try:
        # Получаем имя файла (передаётся как строка)
        file_name = client_socket.recv(1024).decode('utf-8')
        print(f"Получено имя файла: {file_name} от {addr}")

        # Открываем файл для записи бинарных данных
        with open("received_" + file_name, "wb") as f:
            while True:
                bytes_read = client_socket.recv(1024)
                if not bytes_read:
                    break
                f.write(bytes_read)

        print(f"Файл {file_name} успешно получен от {addr}")
    except Exception as e:
        print(f"Ошибка при передаче файла от {addr}: {e}")
    finally:
        client_socket.close()

def start_file_server(host='0.0.0.0', port=12346):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Файловый сервер запущен на {host}:{port} и ожидает подключения...")

    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_file_transfer, args=(client_socket, addr))
        client_thread.start()

if __name__ == '__main__':
    start_file_server()
