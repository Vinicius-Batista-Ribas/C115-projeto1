from socket import *

ServerName = '127.0.0.1'
severPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((ServerName,severPort))

answers = []
for _ in range(3):
    question = clientSocket.recv(1024).decode()
    print(question)
    while True:
        answer = input("Resposta: ").lower()[0]
        if answer in 'abcd':
            break
        print('Alternativa invalida!')
    clientSocket.send(answer.encode())
    response = clientSocket.recv(1024).decode()
    print(response)
    answers.append(answer)

score_response = clientSocket.recv(1024).decode()
print(score_response)
clientSocket.close()