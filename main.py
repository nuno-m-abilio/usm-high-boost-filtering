import sys
import numpy as np
import skimage as ski
from scipy.ndimage import convolve
from os.path import splitext


def mascara_nitidez_high_boost(img_atalho: str, m: int, k: float):
    '''Recebe uma imagem em tons de cinza e dois parâmetros m e k e devolve uma outra imagem em
    tons de cinza aguçada pela aplicação de máscara de nitidez ou filtragem high-boost.'''

    imagem_original = ski.io.imread(img_atalho)

    # Antes precisa garantir que aimagem esteja em tons de cinza
    if imagem_original.ndim == 3:
        imagem_original = ski.color.rgb2gray(imagem_original) * 255
    # e aqui podem aparecer negativos na máscara, mas precisa converter para float
    # para evitar erros de estouro na subtração
    imagem_original = imagem_original.astype(np.float64)  


    # Borra a imagem original com um filtro da média simples m x m usando a função pronta de convolução
    filtro_media = np.ones((m, m), dtype=np.float64) / (m * m)
    imagem_borrada = convolve(imagem_original, filtro_media, mode="reflect")

    # Máscara de nitidez criada pela diferença entre a imagem original e a borrada
    mascara = imagem_original - imagem_borrada

    # Filtragem high-boost
    imagem_agucada = imagem_original + k * mascara

    # Satura os valores fora do intervalo [0, 255] antes de converter para uint8
    imagem_agucada = np.clip(imagem_agucada, 0, 255).astype(np.uint8)

    # Normaliza a máscara apenas para fins de visualização (pq ela possui valores negativos)
    mascara_normalizada = normalizar_para_visualizacao(mascara)

    nome_base, _ = splitext(img_atalho)
    ski.io.imsave(f"{nome_base}_m={m}_k={k}_mascara.jpg", mascara_normalizada)
    ski.io.imsave(f"{nome_base}_m={m}_k={k}_agucada.jpg", imagem_agucada)


def normalizar_para_visualizacao(matriz: np.ndarray) -> np.ndarray:
    '''Normaliza uma matriz com valores quaisquer (negativos também) para o intervalo [0, 255],
    para que possa ser visualizada como uma imagem.'''
    minimo = matriz.min()
    maximo = matriz.max()
    if maximo - minimo == 0: # evita divisão por zero (imagem constante)
        return np.zeros_like(matriz, dtype=np.uint8)
    matriz_normalizada = (matriz - minimo) / (maximo - minimo) * 255
    return matriz_normalizada.astype(np.uint8)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Erro! Modo de uso: python main.py <nome_imagem> <valor_m> <valor_k>")
        sys.exit(1)

    img_atalho = sys.argv[1]
    m = int(sys.argv[2])
    k = float(sys.argv[3])

    if m < 1 or m % 2 == 0:
        print("Erro! O parâmetro m deve ser um número inteiro ímpar e positivo (ex.: 3, 5, 7...)")
        sys.exit(1)

    if k < 0:
        print("Erro! O parâmetro k deve ser maior ou igual a 0")
        sys.exit(1)

    mascara_nitidez_high_boost(img_atalho, m, k)