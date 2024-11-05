import pyautogui
import time

# Função que imprime a posição atual do mouse
def capturar_posicao():
    print("Posicione o cursor onde deseja capturar a coordenada e espere 3 segundos...")
    time.sleep(3)  # Tempo para o usuário posicionar o mouse
    x, y = pyautogui.position()  # Captura as coordenadas do mouse
    print(f"Coordenadas capturadas: X = {x}, Y = {y}")

# Testando a função
capturar_posicao()
