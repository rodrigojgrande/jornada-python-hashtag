# Passo a Passo do Projeto
# Passo 1: Entrar no sistema da empresa
#   https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.3 # Tempo de Pause

# pyautogui.click = Clicar em algum lugar da tela
# pyautogui.write = Escrever um texto
# pyautogui.press = Pressionar 1 tecla do teclado

# pyautogui.hotkey("ctrl","c")

# Abrir o navegador (Chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Dar uma pause de 3 segundos para carregar o site
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=706, y=411, button="left")
pyautogui.write("pythonimpressionador@gmail.com")

# Escrever a senha
pyautogui.press("tab")
pyautogui.write("sua senha aqui")

# Clicar no botão de logar
pyautogui.click(x=959, y=574, button="left")
time.sleep(3)

# Passo 3: Importar base de Dados
# Instalar o pandas -> pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto
# Para cada linha da tabela
for linha in tabela.index:
    # Clicar no primeiro campo
    pyautogui.click(x=760, y=293, button="left")
    
    # Código do Produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # Tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # Categoria
    # str() = Transforma em String
    # Python não aceita escrever o que não é texto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # Preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # Custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Obs
    # Verifica se o campo não está vazio
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): # Verifica se a informação está vazia | NaN - Not a Number
        pyautogui.write(obs)
    pyautogui.press("tab")

    # Enviar
    pyautogui.press("enter")
    
    # Subir a tela
    pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro até acabar a base de dados
