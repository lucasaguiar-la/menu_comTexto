import tkinter as tk
import pyautogui
import keyboard
from functools import partial

menus = {
    "ctrl+alt+z": ["Essa é a nota número 1", "Essa é outra nota", "Mais uma nota que coloquei aqui"],
    "ctrl+alt+x": ["Para essa parte voce coloca essa nota", "Lembre-se, a nota é tal"],
    "ctrl+alt+c": ["Nessa aqui você vai mandar bem", "Deixa de preguiça, só lê a nota aqui", "Nessa pasta você vai arrasar", "Complicade"],
}

# Função para abrir o menu
def show_menu(texts):
    x, y = pyautogui.position()  # Pega posição do mouse
    
    # Cria janela sem borda
    menu = tk.Toplevel(root)
    menu.overrideredirect(True)
    menu.geometry(f"+{x}+{y}")  # Posição na tela
    menu.attributes('-topmost', True)  # Mantém a janela acima de todas
    
    # Adiciona cada texto como um label
    for text in texts:
        lbl = tk.Label(menu, text=text, anchor="w", bg="white", fg="black", 
                        padx=10, pady=5, relief="solid", borderwidth=1)
        lbl.pack(fill="x")

    # Atalho para fechar o menu
    def fechar_menu():
        if menu.winfo_exists():
            menu.destroy()
    keyboard.add_hotkey("ctrl+alt+\\", fechar_menu)

    # Garante que o Tk aplique a posição
    menu.update_idletasks()

# Configura os atalhos usando partial para "fixar" cada lista
for hotkey, texts in menus.items():
    keyboard.add_hotkey(hotkey, partial(show_menu, texts))

# Janela oculta (loop principal)
root = tk.Tk()
root.withdraw()

print("Atalhos ativos:")
for hotkey in menus.keys():
    print(f"  {hotkey}")

root.mainloop()
