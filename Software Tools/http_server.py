"""
    Multi Threaded Http server which accept request from multiple client
    and process request concurrently.
"""

import socket
import time
from datetime import datetime
import concurrent.futures as cf

def current_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    return formatted_time

def handle_client(client_socket):
    try :
        request = client_socket.recv(1024).decode("utf-8")
        print(f"[{current_time()}]: processing client request ...\n{request}")
        time.sleep(10)
        client_socket.sendall(b"HTTP/1.1 200 OK\r\n\r\nHello, World!\r\n")
    except Exception as e:
        print(f"[{current_time()}] Error handling client: {e}")
    finally:
        client_socket.close()

def main():
    with socket.create_server(("localhost",1729)) as server_socket:
        server_socket.listen()
        print(f"[{current_time()}]: http server is listening on port 1729...")  
        with cf.ThreadPoolExecutor() as executor:
            while True:  
                client_socket,addr = server_socket.accept()
                print(f"[{current_time()}]: client connected with {addr}")
                executor.submit(handle_client, client_socket)
                
if __name__ == "__main__":
    main()
