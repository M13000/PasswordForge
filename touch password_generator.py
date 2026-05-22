import random
import string

print("=== PasswordForge - Gerador de Senhas ===")

tamanho = int(input("Digite o tamanho da sua senha: "))

quantidade = int(input("Digite quantas senhas deseja criar: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

for i in range(quantidade):
    senha = ""
    
    for j in range(tamanho):
        senha += random.choice(caracteres)
    
    print(f"Senha gerada: {senha}")