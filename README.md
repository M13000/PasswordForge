# PasswordForge
Gerador de senhas seguras — projeto de aprendizado em cibersegurança.

---

## Sobre

Criei essa ferramenta depois de estudar como ataques de dicionário funcionam na prática. Quando você vê 14 milhões de senhas vazadas numa wordlist, fica óbvio por que a maioria das pessoas tá completamente exposta.

O PasswordForge usa o módulo `secrets` do Python, que gera senhas com entropia criptográfica real — diferente do módulo `random`, que é determinístico e não deveria chegar perto de nada relacionado à segurança.

---

## Como usar

```bash
python3 password_forge.py
```

Digite o tamanho desejado e a quantidade de senhas. O programa gera senhas com letras, números e caracteres especiais.

---

## Por que `secrets` e não `random`?

O módulo `random` do Python é determinístico: dado o mesmo estado inicial, sempre produz a mesma sequência. Isso o torna completamente inadequado para criptografia ou geração de senhas.

O módulo `secrets` usa fontes de entropia do sistema operacional, tornando as senhas geradas verdadeiramente imprevisíveis.

---

## Contexto

Esse projeto faz parte da minha transição de carreira para cibersegurança. Tô aprendendo de forma autônoma, construindo ferramentas reais pra fixar os conceitos na prática — porque tutorial sem projeto não cola.

Conforme avanço nos estudos, continuo melhorando e adicionando funcionalidades.

---

23 anos. Logística de dia, cibersegurança de noite.
