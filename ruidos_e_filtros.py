import cv2
import numpy as np

def aplicar_ruido_sal_pimenta(img):
    # Aplica ruído sal e pimenta
    row, col = img.shape
    num_pixels = int(row * col * 0.02)  # quantidade de pixels com ruído

    for _ in range(num_pixels):
        y_coord = np.random.randint(0, row)
        x_coord = np.random.randint(0, col)
        img[y_coord, x_coord] = 0  # ponto preto
        y_coord = np.random.randint(0, row)
        x_coord = np.random.randint(0, col)
        img[y_coord, x_coord] = 255  # ponto branco

    return img

def aplicar_ruido_gaussiano(img):
    # Aplica ruído gaussiano
    row, col = img.shape
    mean = 0
    sigma = 25
    gauss = np.random.normal(mean, sigma, (row, col)).reshape(row, col)
    img_gauss = cv2.add(img, gauss.astype('uint8'))
    return img_gauss

def filtro_media(img):
    # Aplica filtro de média
    return cv2.blur(img, (5, 5))

def filtro_mediana(img):
    # Aplica filtro de mediana
    return cv2.medianBlur(img, 5)

def filtro_bilateral(img):
    # Aplica filtro bilateral
    return cv2.bilateralFilter(img, 9, 75, 75)
