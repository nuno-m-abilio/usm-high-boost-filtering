# usm-high-boost-filtering

Este projeto implementa o algoritmo de Máscara de Nitidez e Filtragem High-Boost em tons de cinza, baseado na Seção 3.6.3 do livro do Gonzalez-Woods (3ª ed.). O programa aplica um filtro de média simples de tamanho $m \times m$ e pondera o realce das bordas com um fator de ganho $k$.

## Pré-requisitos e Bibliotecas

Antes de rodar o código, você precisa ter o Python 3.x instalado e baixar as bibliotecas necessárias para o processamento de imagens e matrizes.

Para instalar todas de uma vez, abra o seu terminal e rode o comando:

```bash
pip install numpy scikit-image scipy

```

## Como Rodar o Código

O programa funciona via linha de comando (terminal). Ele recebe 3 argumentos obrigatórios nesta ordem:

1. O nome/caminho da imagem de entrada.
2. O valor de **m** (tamanho da máscara: deve ser um número inteiro, ímpar e positivo, ex: 3, 5, 7, 13...).
3. O valor de **k** (fator de ganho: número real maior ou igual a 0).

### Exemplo de uso no terminal:

```bash
python main.py blurry_moon.tif 5 3.0

```

## Organização das Saídas

As imagens resultantes (a máscara de nitidez calculada e a imagem final aguçada) serão salvas automaticamente dentro da pasta **`figure/`** com os parâmetros organizados no nome do arquivo:

* `figure/blurry_moon_m=5_k=3.0_mascara.jpg`
* `figure/blurry_moon_m=5_k=3.0_agucada.jpg`

```