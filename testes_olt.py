import telnetlib, time


HOST = str('172.31.0.21')  # Endereço do dispositivo Telnet
PORT = 23  # Porta Telnet padrão

# Obter nome de usuário e senha do usuário
username = 'admin'
password = 'admin'

# Criar objeto Telnet e conectar ao dispositivo
tn = telnetlib.Telnet(HOST, PORT)

# Fazer login
tn.read_until(b"olt8820plus login: ")
tn.write(username.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(1)  # Aguardar um segundo após enviar a senha


comando = f"onu delete gpon 1 onu 6"
comando2 = 'yes'
comando3 = 'no'

tn.write(f"{comando}\n".encode('ascii'))

# Aguardar a resposta
time.sleep(1)

# Ler a resposta até encontrar o prompt novamente
resultado = tn.read_until(b"olt8820plus login:", timeout=5).decode('ascii')
print(resultado)

tn.write(f"{comando2}\n".encode('ascii'))

# Aguardar a resposta
time.sleep(1)

# Ler a resposta até encontrar o prompt novamente
resultado = tn.read_until(b"olt8820plus login:", timeout=5).decode('ascii')

#linhas = resultado.splitlines()[-2].split()
print(resultado)





tn.write(f"{comando3}\n".encode('ascii'))

# Aguardar a resposta
time.sleep(1)

# Ler a resposta até encontrar o prompt novamente
resultado = tn.read_until(b"olt8820plus login:", timeout=5).decode('ascii')

print(resultado)







tn.write(f"{comando2}\n".encode('ascii'))

# Aguardar a resposta
time.sleep(1)

# Ler a resposta até encontrar o prompt novamente
resultado = tn.read_until(b"olt8820plus login:", timeout=5).decode('ascii')

print(resultado)