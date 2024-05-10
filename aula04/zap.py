#Estrutura do site

#Título: Debzap
#Botão de iniciar Chat
    #popup (Janela na frente da tela)
        #título: Bem vindo ao debzap
        #campo de texto: escreva seu nome no chat
        #botão: entrar no chat
            #Sumir com o título debzap
            #fechar janela popup
            #carregar o chat
                #mensagens que já foram enviadas
                #campo: digite sua mensagem
                #botão de enviar

import flet as ft

#criar função principal do seu app
def main(pagina):

    titulo = ft.Text("DebZap")

    chat = ft.Column()
    mensagem_usuario = ft.TextField(label="Escreva aqui sua mensagem")

    def enviar_mensagem(evento):
        texto_mensagem = mensagem_usuario.value
        nome_usuario1 = nome_usuario.value
        mensagem = f"{nome_usuario1}: {texto_mensagem}"
        pagina.pubsub.send_all(mensagem)
        mensagem_usuario.value = ""
        pagina.update()

    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_mensagem = ft.Row([mensagem_usuario, botao_enviar_mensagem])


    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        msg_entrou_chat = f"{nome_usuario.value} entrou no chat."
        pagina.pubsub.send_all(msg_entrou_chat)
        pagina.update()


    titulo_janela = ft.Text("Bem vindo ao DebZap")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_janela = ft.ElevatedButton("Entrar no chat", on_click= entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=nome_usuario,actions=[botao_janela])

    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()


    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click= iniciar_chat)

    pagina.add(titulo)
    pagina.add(botao_iniciar)


    #criar túnel de comunicação (websocket)
    def funcao_comunicacao(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()

    pagina.pubsub.subscribe(funcao_comunicacao)

#rodar o app
ft.app(main, view = ft.WEB_BROWSER)
    
