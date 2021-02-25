from socket import *

def smtp_client(port = 1025, mailserver = "127.0.0.1"): #Fill in start #Fill in end
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    
    recv = clientSocket.recv(1024).decode()

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    
    # Send MAIL FROM command and print server response.
    mailFrom = "MAIL FROM: <jeg9979@nyu.edu>\r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    
    # Send RCPT TO command and print server response.
    rcptTo = "RCPT TO: <jean.graham@stonybrook.edu>\r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    
    # Send DATA command and print server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    #recv4 = clientSocket.recv(1024).decode()
    
    # Send message data.
    clientSocket.send(msg.encode())
    recv5 = clientSocket.recv(1024).decode()
    
    # Message ends with a single period.
    clientSocket.send(endmsg.encode())
    recv6 = clientSocket.recv(1024).decode()
    
    # Send QUIT command and get server response.
    quitCommand = "QUIT\r\n"
    clientSocket.send(quitCommand.encode())
    recv7 = clientSocket.recv(1024).decode()
    
    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
