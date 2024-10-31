# Problema: Equilíbrio da Gangorra

## Descrição
Este problema consiste em verificar o equilíbrio de uma gangorra assimétrica, onde uma das extremidades é mais longa que a outra. O equilíbrio é determinado pela fórmula:

\[
P1 \times C1 = P2 \times C2
\]

onde:
- `P1` é o peso da criança na extremidade esquerda da gangorra,
- `C1` é o comprimento da extremidade esquerda da gangorra,
- `P2` é o peso da criança na extremidade direita da gangorra,
- `C2` é o comprimento da extremidade direita da gangorra.

### Regras para o equilíbrio:
- A gangorra estará equilibrada se o produto do peso pelo comprimento for igual em ambas as extremidades, ou seja, se \( P1 \times C1 = P2 \times C2 \).
- Se o momento no lado esquerdo (`P1 * C1`) for maior que o do lado direito (`P2 * C2`), a gangorra inclina para o lado esquerdo, e a saída deve ser `-1`.
- Se o momento no lado direito (`P2 * C2`) for maior que o do lado esquerdo (`P1 * C1`), a gangorra inclina para o lado direito, e a saída deve ser `1`.

## Entrada
- Uma linha contendo quatro inteiros `P1`, `C1`, `P2`, e `C2`, onde:
  - \(10 \leq P1, C1, P2, C2 \leq 100\).

## Saída
- Imprima `0` se a gangorra estiver equilibrada,
- Imprima `-1` se o lado esquerdo estiver mais baixo,
- Imprima `1` se o lado direito estiver mais baixo.

## Exemplos

### Exemplo 1
**Entrada**
```
30 100 60 50
```

**Saída**
```
0
```
**Explicação:** O produto `P1 * C1` é igual a `P2 * C2`, portanto, a gangorra está equilibrada.

### Exemplo 2
**Entrada**
```
40 40 38 60
```

**Saída**
```
1
```
**Explicação:** O produto `P2 * C2` é maior que `P1 * C1`, então o lado direito fica mais baixo.

### Exemplo 3
**Entrada**
```
35 80 35 75
```

**Saída**
```
-1
```
**Explicação:** O produto `P1 * C1` é maior que `P2 * C2`, então o lado esquerdo fica mais baixo.

## Solução

Para resolver o problema:
1. Calcule o momento em cada extremidade da gangorra:
   - `momento_esquerdo = P1 * C1`
   - `momento_direito = P2 * C2`
2. Compare os valores dos momentos:
   - Se `momento_esquerdo` for igual a `momento_direito`, imprima `0`.
   - Se `momento_esquerdo` for maior que `momento_direito`, imprima `-1`.
   - Se `momento_direito` for maior que `momento_esquerdo`, imprima `1`.

### Código em Python

```python
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
```

### Explicação do Código
- Lemos e convertemos os valores de entrada em inteiros.
- Calculamos os momentos de cada lado da gangorra multiplicando o peso pelo comprimento.
- Comparamos os momentos e imprimimos o resultado:
  - `0` se estiver equilibrada,
  - `-1` se o lado esquerdo for mais baixo,
  - `1` se o lado direito for mais baixo.

### Complexidade
O programa tem complexidade **O(1)**, pois todas as operações de leitura, cálculo e comparação têm tempo constante.
