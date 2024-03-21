# Hashzap
# botao de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem


# produto = {
#     "nome": "iphone",
#     "preço": 6500,
#     "quantidade": 150    
# }

# produto["quantidade"]

# Frameworks do Python -  Conjunto de Ferramentas
# Flet
# Django
# Flesk

# Instalar o Flet
# pip install flet

# Importa o Flet
import flet as ft # Framework

# Define uma função principal / main
def main(pagina): # Vai chamar a página pagina
    texto = ft.Text("Hashzap") # Cria um texto
    
    chat = ft.Column() # Cria o chat
    
    def enviar_mensagem_tunel(mensagem): # Manda a mensagem para todos pelo tunel
        print(mensagem)
        # Adicione a mensagem no chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem) # Adiciona uma informação a um campo existente
        pagina.update() # Atualizar a edição visual

    
    def enviar_mensagem(evento): 
        print("Enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}") # Envia a mensagem para todos com nome do usuario e mensagem
        
        # Limpe o campo mensagem
        campo_mensagem.value = ""
        pagina.update() # Atualizar a edição visual
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel) # Túnel de comunicação da aplicação (Socket, Websocket)
        
    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem) # Cria campo de enviar mensagem
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem) # Cria botão de enviar
    linha_enviar = ft.Row([campo_mensagem, botao_enviar]) # Cria uma linha
    
    def entrar_chat(evento): # Vai chamar a página pagina
        # Feedback Terminal
        print("Entrar no chat")
        # Fechar o popup
        popup.open = False
        
        # Tirar o botão iniciar chat
        pagina.remove(botao_iniciar)
        
        # Tirar o título Hashzap
        pagina.remove(texto)
        
        # Criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat") # Informa para todos que o usuário entrou no chat
        # chat.controls.append(texto_entrada) # Adiciona uma informação a um campo existente
        
        # Colocar o campo de digitar  mensagem
        # pagina.add(campo_mensagem)
        
        # Criar o botão de enviar
        # pagina.add(botao_enviar)
        pagina.add(linha_enviar)
        pagina.update()
    
    # Variaveis Popup
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    # Define um popup
    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    ) 

    def abrir_popup(evento): # Evento ao clicar ao botão
        # print("abrir o chat")
        pagina.dialog = popup
        popup.open = True # Abre o popup
        pagina.update() # Atualiza o visual da página sem F5
            
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup) # Cria um botão
    
    pagina.add(texto) # Adiciona o texto
    pagina.add(botao_iniciar) # Adiciona o botao

ft.app(target=main, view=ft.WEB_BROWSER) # Criar o app chamando a função principal (Com visualização WEB)
