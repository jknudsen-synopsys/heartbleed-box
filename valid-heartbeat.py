import socket

tls_hello_s = "1603020034010000300302615d9acb434f4445434f4445434f4445434f4445434f4445434f4445434f4445000002002f01000005ff01000100"
tls_hello = bytes.fromhex(tls_hello_s)

tls_heartbeat_s = "1803020013010010BEEF0000BEEF1111BEEF2222BEEF3333BEEF4444BEEF5555BEEF6666BEEF7777"
tls_heartbeat = bytes.fromhex(tls_heartbeat_s)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 4433)
print('[Connecting to {} port {}]'.format(*server_address))
s.connect(server_address)

try:
    s.sendall(tls_hello)     # Send Client Hello
    s.recv(8 * 1024)         # Receive Server Hello, Certificate, Server Hello Done
    s.sendall(tls_heartbeat) # Send correctly formed Heartbeat Request
    r = s.recv(1024)         # Receive Heartbeat Response

    print(bytes.hex(r))
    

finally:
    print('[Closing socket]')
    s.close()