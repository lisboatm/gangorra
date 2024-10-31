# Leitura da entrada
P1, C1, P2, C2 = map(int, input().split())

# Calcula os momentos de cada lado
momento_esquerdo = P1 * C1
momento_direito = P2 * C2

# Compara os momentos e imprime o resultado
if momento_esquerdo == momento_direito:
    print(0)
elif momento_esquerdo > momento_direito:
    print(-1)
else:
    print(1)
