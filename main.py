import cv2
import matplotlib.pyplot as plt
from ruidos_e_filtros import (
    aplicar_ruido_sal_pimenta, 
    aplicar_ruido_gaussiano, 
    filtro_media, 
    filtro_mediana, 
    filtro_bilateral
)

# Carrega a imagem original em grayscale
imagem = cv2.imread('gato2.jpeg', cv2.IMREAD_GRAYSCALE)

# Verifica se a imagem foi carregada
if imagem is None:
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho do arquivo.")
    exit()

# Aplica os ruídos
imagem_sal_pimenta = aplicar_ruido_sal_pimenta(imagem.copy())
imagem_gaussiano = aplicar_ruido_gaussiano(imagem.copy())
imagem_gaussiano_sal_pimenta = aplicar_ruido_gaussiano(aplicar_ruido_sal_pimenta(imagem.copy()))

# Aplica os filtros para cada tipo de ruído
filtros = {
    "Filtro de Média": filtro_media,
    "Filtro de Mediana": filtro_mediana,
    "Filtro Bilateral": filtro_bilateral
}

# Define imagens para a grade
imagens = [
    #(imagem, "Imagem Original (Preto e Branco)"),
    
    (imagem_sal_pimenta, "Ruído: Sal e Pimenta"),
    (filtros["Filtro de Média"](imagem_sal_pimenta), "Sal e Pimenta + Filtro Média"),
    (filtros["Filtro de Mediana"](imagem_sal_pimenta), "Sal e Pimenta + Filtro Mediana"),
    (filtros["Filtro Bilateral"](imagem_sal_pimenta), "Sal e Pimenta + Filtro Bilateral"),
    
    (imagem_gaussiano, "Ruído: Gaussiano"),
    (filtros["Filtro de Média"](imagem_gaussiano), "Gaussiano + Filtro Média"),
    (filtros["Filtro de Mediana"](imagem_gaussiano), "Gaussiano + Filtro Mediana"),
    (filtros["Filtro Bilateral"](imagem_gaussiano), "Gaussiano + Filtro Bilateral"),
    
    (imagem_gaussiano_sal_pimenta, "Ruído: Gaussiano + Sal e Pimenta"),
    (filtros["Filtro de Média"](imagem_gaussiano_sal_pimenta), "Gaussiano + Sal e Pimenta + Filtro Média"),
    (filtros["Filtro de Mediana"](imagem_gaussiano_sal_pimenta), "Gaussiano + Sal e Pimenta + Filtro Mediana"),
    (filtros["Filtro Bilateral"](imagem_gaussiano_sal_pimenta), "Gaussiano + Sal e Pimenta + Filtro Bilateral")
]

# Ajusta a quantidade de imagens na grade para evitar eixos vazios
fig, axs = plt.subplots(4, 4, figsize=(15, 15))
fig.suptitle("Comparação de Ruídos e Filtros", fontsize=16)

# Exibe as imagens sem os eixos
for i, (img, title) in enumerate(imagens):
    ax = axs[i // 4, i % 4]
    ax.imshow(img, cmap='gray')
    ax.set_title(title, fontsize=10)
    ax.axis('off')  # Desativa completamente os eixos

# Remove eixos não utilizados
for j in range(i + 1, 16):
    fig.delaxes(axs[j // 4, j % 4])

plt.tight_layout()
plt.subplots_adjust(top=0.92)  # Ajuste do espaço para o título
plt.show()
