import socket  # noqa: F401


def main():

    with socket.create_server(("localhost", 8080), reuse_port=True) as server_socket:

        connection, address = server_socket.accept() # wait for client

        print(f"accepted connection from {address}")

        connection.sendall("HTTP/1.1 200 OK\r\n\r\n".encode("utf-8"))

if __name__ == "__main__":
    main()
