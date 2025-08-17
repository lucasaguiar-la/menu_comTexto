import tkinter as tk
import pyautogui
import keyboard

# Dicionário: cada atalho → lista de textos
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
    
    # SOLUÇÃO 1: Definir posição ANTES do topmost
    menu.geometry(f"+{x}+{y}")
    menu.update_idletasks()  # Força atualização da geometria
    menu.attributes('-topmost', True)  # Aplica topmost DEPOIS
    
    # Adiciona cada texto como um label
    for text in texts:
        lbl = tk.Label(menu, text=text, anchor="w", bg="white", fg="black", 
                        padx=10, pady=5, relief="solid", borderwidth=1)
        lbl.pack(fill="x")
        
        # Adiciona função de clique para copiar texto
        lbl.bind("<Button-1>", lambda e, txt=text: copy_to_clipboard(txt, menu))

    def fechar_menu():
        if menu.winfo_exists():
            menu.destroy()
    
    keyboard.add_hotkey("ctrl+alt+\\", fechar_menu)

    # Fecha se perder o foco (com delay para evitar fechamento imediato)
    menu.after(100, lambda: menu.bind("<FocusOut>", lambda e: menu.destroy()))
    menu.focus_force()

def copy_to_clipboard(text, menu):
    """Copia texto para clipboard e fecha o menu"""
    pyautogui.hotkey('ctrl', 'c')  # Limpa clipboard atual
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    menu.destroy()

# Configura os atalhos
for hotkey, texts in menus.items():
    keyboard.add_hotkey(hotkey, lambda t=texts: show_menu(t))

# Janela oculta (loop principal)
root = tk.Tk()
root.withdraw()

print("Atalhos ativos:")
for hotkey in menus.keys():
    print(f"  {hotkey} → abre menu")
print("  ctrl+alt+\\ → fecha menu")
print("  Clique em qualquer item para copiar para clipboard")

root.mainloop()