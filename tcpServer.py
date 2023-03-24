import socket

def main():
    host = '127.0.0.1'
    port = 4000

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, address = s.accept()
    print ("Connection from "+ str(address))
    
    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("From connection user: "+data)
        data = data.upper()
        print("Sending: "+ data)
        c.send(data.encode('utf-8'))
    c.close()

if __name__ == '__main__':
    main()
