# PasswordForge

Gerador de senhas seguras desenvolvido como projeto de aprendizado em ciberseguranca.

---

## Sobre

Criei essa ferramenta depois de estudar como ataques de dicionario funcionam na pratica. Quando voce vê 14 milhoes de senhas vazadas numa wordlist, entende rapidamente que a maioria das pessoas escolhe senhas fracas e previsiveis.

O PasswordForge usa o modulo secrets do Python, que gera senhas com entropia criptografica real — diferente do modulo random, que é presível e não deve ser usado para fins de segurança.

---

## Como usar

```bash
python3 password_forge.py
```

Digite o tamanho desejado e a quantidade de senhas. O programa gera senhas com letras, números e caracteres especiais.

---

## Por que secrets e nao random?

O modulo random do Python é deterministico, dado o mesmo estado inicial, sempre gera a mesma sequencia. Isso o torna inadequado para criptografia e geracao de senhas.

O modulo secrets usa fontes de entropia do sistema operacional, tornando as senhas geradas verdadeiramente imprevisíveis.

---

## Nota

Este projeto faz parte da minha jornada de transição de carreira para ciberseguranca. Estou aprendendo de forma autonoma, construindo ferramentas reais pra fixar os conceitos na pratica.

Conforme avanço nos estudos, continuo melhorando e adicionando funcionalidades.

---

23 anos. Logistica de dia, ciberseguranca de noite.
