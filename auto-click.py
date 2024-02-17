import pyautogui
import keyboard
import time

print("Pressione F8 para iniciar ou parar os cliques do mouse.")

clicando = False


def on_f8_pressed():
    global clicando
    clicando = not clicando
    if clicando:
        print("Clicando. Pressione F8 para parar.")
    else:
        print("Parado. Pressione F8 para iniciar os cliques novamente.")


# Configura o evento para escutar a tecla F8
keyboard.add_hotkey("F8", on_f8_pressed)

# Loop principal do script
try:
    while True:
        time.sleep(0.1)  # Pequena pausa para evitar uso excessivo da CPU
        if clicando:
            pyautogui.click(button='right')
            time.sleep(0.3)  # Espera 0.3 segundo entre os cliques
except KeyboardInterrupt:
    print("Script interrompido.")
