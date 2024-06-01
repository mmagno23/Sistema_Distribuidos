import random
import time

inicio = time.time()
controle = 1

chaveP = (2**127) - 1
chave = (2**24) - 1

# Encontrar um valor de P que satisfaça as condições
while controle == 1:
    n = random.randrange(32, chaveP)
    t1 = pow(2, n-1, n)
    t2 = pow(3, n-1, n)
    t3 = pow(4, n-1, n)
    t4 = pow(5, n-1, n)
    t5 = pow(6, n-1, n)
    if (t1 == 1) and (t2 == 1) and (t3 == 1) and (t4 == 1) and (t5 == 1):
        P = n
        controle = 0

print("Valor de P:", P)

# Encontrar um valor de g que seja menor que P
g = random.randrange(32, P-1)
print("Valor de g:", g)

# Gerar chaves privadas aleatórias a e b
a = random.randrange(127, chave)
b = random.randrange(127, chave)
print("Valor de a:", a)
print("Valor de b:", b)

# Calcular chaves públicas A e B
A = pow(g, a, P)
B = pow(g, b, P)
print("Chave A:", A)
print("Chave B:", B)

# Calcular a chave simétrica compartilhada k1 e k2
k1 = pow(B, a, P)
k2 = pow(A, b, P)
print("Chave simétrica k1:", k1)
print("Chave simétrica k2:", k2)

assert k1 == k2, "As chaves simétricas não coincidem!"
# Marcar o tempo até este ponto
fim = time.time()
tempo_total_segundos = fim - inicio
print("O tempo total para geração das chaves foi:", tempo_total_segundos," segundos ")

# Iniciar o tempo para a quebra da chave
inicio_quebra = time.time()

# Tentativa de quebra por força bruta
for quebra in range(127, chave):
    kebra = pow(B, quebra, P)
    if k1 == kebra:
        fim_quebra = time.time()
        tempo_quebra_segundos = fim_quebra - inicio_quebra
        print("Quebra concluída, chave privada encontrada:", quebra)
        print("Tempo total em  para quebrar a chave:", tempo_quebra_segundos, " Segundos")
        break
