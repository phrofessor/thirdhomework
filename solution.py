from socket import *

import smtplib 

def smtp_client(port = 1025, mailserver = "127.0.0.1"): #Fill in start #Fill in end
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    
    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond Gradescope
    #mailserver = ("127.0.0.1".encode(), 1025)
    
    # Create socket called clientSocket and establish a TCP connection with mailserver
    # This is the first step. 220 means the connection is successful
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    if recv[:3] != '220':
        #print('220 reply not received from server.')
    elif recv[:3] == "220":
        #print("Success 220")

    # Send HELO command and print server response.
    # This is the SMTP handshake. 250 means the handshake is successful
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        #print('250 reply not received from server.')
    elif recv1[:3] == "250":
        #print("Success 1")
    
    # Send MAIL FROM command and print server response.
    # Still in the handshaking phase. Specify the sender
    # mailserver.starttls()
    mailFrom = "MAIL FROM: jeg9979@nyu.edu\r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    if recv2[:3] != "250":
        #print("250 reply not received from server.")
    elif recv[:3] == "250":
        #print("Success 2")
    
    # Send RCPT TO command and print server response.
    # Still in the handshaking phase. Specify the recipient
    rcptTo = "RCPT TO: <jean.graham@stonybrook.edu> \r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    if recv3[:3] != "250":
        #print("250 reply not received from server.")
    elif recv[:3] == "250":
        #print("Success 3")
    
    # Send DATA command and print server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)
    if recv4[:3] != "250":
        #print("250 reply not received from server.")
    elif recv4[:3] == "250":
        #print("Success 4")
    
    # Send message data.
    clientSocket.send(msg.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print(recv5)
    if recv5[:3] != "250":
        #print("250 reply not received from server.")
    elif recv[:3] == "250":
        #print("Success 5")
    
    # Message ends with a single period.
    clientSocket.send(endmsg.encode())
    recv6 = clientSocket.recv(1024).decode()
    #print(recv6)
    if recv6[:3] != "250":
        #print("250 reply not received from server.")
    elif recv[:3] == "250":
        #print("Success 6")
    
    # Send QUIT command and get server response.
    quitCommand = "QUIT\r\n"
    clientSocket.send(quitCommand.encode())
    recv7 = clientSocket.recv(1024).decode()
    #print(recv7)
    #print("Success 7")
    #changes
    
    clientSocket.close()

if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')
