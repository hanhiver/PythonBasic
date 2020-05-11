from multiprocessing.connection import Listener
from array import array

address = ('localhost', 6000)
with Listener(address, authkey = b'secret password') as listener:
    with listener.accept() as conn:
        print('Connection accepted from', listener.last_accepted)
        
        conn.send([2.25, None, 'junk', float])
        conn.send_bytes(b'hello')
        conn.send_bytes(array('i', [42, 1729]))

        print(conn.recv())

