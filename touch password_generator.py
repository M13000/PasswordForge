import random
import string
import secrets

print("=== PasswordForge - Gerador de Senhas ===")

tamanho = int(input("Digite o tamanho da sua senha: "))

quantidade = int(input("Digite quantas senhas deseja criar: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

print(f"\n{quantidade} senha(s) gerada(s):\n")

for i in range(1, quantidade + 1):
    senha = "".join(secrets.choice(caracteres) for _ in range(tamanho))
    print(f"[{i}] {senha}")
    
print("\nDica: use um gerenciador de senhas para armazenar elas com segurança.")