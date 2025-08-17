# Menu Com Texto

Este projeto é um utilitário Python para criar um menu de contexto personalizado no Windows.

## Requisitos
- Python 3.7 ou superior
- pip
- Windows

## Passo a passo para rodar o projeto

### 1. Crie e ative um ambiente virtual (venv)
Abra o terminal na pasta do projeto e execute:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 2. Instale as dependências

```powershell
pip install -r requirements.txt
```

### 3. Execute o projeto

```powershell
python main.py
```

### 4. Compilando o projeto com PyInstaller

Para gerar o executável, execute:

```powershell
pyinstaller menu_contexto.spec
```

O executável será gerado na pasta `dist`.

---

By: 
<img src="./kirby.png" alt="deusAbelha" style="width: 80px;">