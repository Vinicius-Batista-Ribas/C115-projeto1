from socket import *
import psycopg2

def BD():
    # CONEXAO AO BANCO DE DADOS
    dbname = 'root'
    user = 'root'
    password = 'root'
    host='172.19.0.2'
    port='5432'

    conection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    # PEGANDO AS PERGUNTAS
    cursor = conection.cursor()
    cursor.execute("SELECT quest FROM c115")
    rows = cursor.fetchall()
    perguntas = [row[0] for row in rows]

    # PEGANDO AS RESPOSTAS
    cursor.execute("SELECT answer FROM c115")
    rows = cursor.fetchall()
    respostas = [row[0] for row in rows]
    cursor.close()
    conection.close()
    return(perguntas, respostas)
    




host = '127.0.0.1'
Server_Port = 12000

# DEFININDO PORTA PARA CONEXÃO COM CLIENTE
SocketServer = socket(AF_INET, SOCK_STREAM)
SocketServer.bind((host,Server_Port))
SocketServer.listen()

quest, answer = BD()
Score = 0

print("server Ready")
client_socket, client_addres = SocketServer.accept()
print("conexão estabelecida")
# MANDANDO AS PERGUNTAS E RECEBENDO AS RESPOSTAS
for i, question in enumerate(quest):
        client_socket.send(question.encode())
        client_response = client_socket.recv(1024).decode().strip()
        if client_response.lower() == answer[i]:
            client_socket.send("Resposta correta!\n".encode())
            Score += 1
        else:
            client_socket.send("Resposta incorreta.\nResposta correta alternativa: {}".format(answer[i]).encode())


client_socket.send(f"Você acertou {Score} questões.\n".encode())
# FECHANDO SERVIDOR
client_socket.close()
SocketServer.close()
