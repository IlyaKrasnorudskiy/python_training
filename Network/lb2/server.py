import socket
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Сервер запущен и ожидает подключения...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Подключен клиент: {addr}")
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Получено сообщение: {data}")
        client_socket.send("Сообщение получено".encode('utf-8'))
        client_socket.close()

start_server()
