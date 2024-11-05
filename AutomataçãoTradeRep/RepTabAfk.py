import pyautogui
import time

# Desativar FAILSAFE
pyautogui.FAILSAFE = False

def realizar_acao(x1, y1, x2, y2, x3, y3, mensagem="!"+"trade rep tabbbbbbbb"):
    print("Iniciando script...")

    # Mover o mouse para a primeira posição e clicar
    pyautogui.moveTo(x1, y1, duration=1)
    time.sleep(0.5)
    pyautogui.click()
    print("Clicou na primeira posição.")

    # Espera um tempo após abrir o jogo
    time.sleep(3)  # Espera para garantir que o jogo esteja pronto

    # Mover o mouse para a segunda posição e clicar
    pyautogui.moveTo(x2, y2, duration=1)
    time.sleep(0.5)
    pyautogui.click()
    print("Clicou na segunda posição.")

    # Digitar a mensagem e pressionar Enter
    pyautogui.press('enter')
    pyautogui.write(mensagem)
    
    time.sleep(5)
    
    pyautogui.press('enter')
    
    print("Mensagem enviada.")
    
    time.sleep(20)
    
    # Mover o mouse para a terceira posição e clicar
    pyautogui.moveTo(x3, y3, duration=1)
    time.sleep(0.5)
    pyautogui.mouseDown(x3, y3)  # Pressiona o botão do mouse na terceira posição
    time.sleep(0.1)  # Pequeno atraso entre o mouseDown e mouseUp
    pyautogui.mouseUp(x3, y3)  # Solta o botão do mouse na terceira posição

    print("Clicou na terceira posição.")
    
    # Pressionar Alt + Esc para minimizar ou mudar de janela
    time.sleep(10)  # Esperar 1 segundo antes de simular as teclas
    pyautogui.hotkey('alt', 'esc')
    print("Pressionou Alt + Esc para minimizar.")

# Coordenadas da ação
x1 = 713  # primeira posição
y1 = 740
x2 = 686  # segunda posição
y2 = 344
x3 = 647  # terceira posição
y3 = 439

# Executar la acción en un bucle cada 1 hora y 3 minutos
while True:
    realizar_acao(x1, y1, x2, y2, x3, y3)
    print("Esperando 1 hora e 3 minutos para a próxima execução...")
    time.sleep(3780)  # Esperar 1 hora e 3 minutos (3600 + 180 segundos)
