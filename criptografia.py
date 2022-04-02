import rsa

chave_publica, chave_privada = rsa.newkeys(512)

mensagem = input("Escreva uma mensagem: ")

string_criptografada = rsa.encrypt(mensagem.encode(), chave_publica)

string_descriptografada = rsa.decrypt(
    string_criptografada, chave_privada).decode()
print("Mensagem informada inicialmente: ", mensagem)
print("Mensagem criptografada: ", string_criptografada)
print("Mensagem descriptografada: ", string_descriptografada)
