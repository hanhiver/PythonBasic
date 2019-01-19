from multiprocessing.connection import Client
from array import array

address = ('localhost', 6000)

with Client(address, authkey=b'secret password') as conn:
    print(conn.recv())
    print(conn.recv_bytes())
    
    arr = array('i', [0, 0, 0, 0, 0])
    print(conn.recv_bytes_into(arr))
    print(arr)

    conn.send(b'Hello! Server! -- From client')

