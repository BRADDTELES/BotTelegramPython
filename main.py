#pip install pytelegrambotapi
#CONEXÃO
import telebot

# EXEMPLO_DE_CHAVE_API = "875d41ss5236D52:54125-A5564125"
CHAVE_API = "coloque sua chave aqui"

bot = telebot.TeleBot(CHAVE_API)

#CRIAR AS MENSAGENS AUTOMATICAS DO TELE-ATENDIMENTO

@bot.message_handler(commands=["linguagem"])
def linguagem(mensagem):
    bot.send_message(mensagem.chat.id, "O Python possui uma comunidade vasta e ativa de desenvolvedores, o que significa que você encontrará muitos recursos online, tutoriais e fóruns para ajudá-lo a solucionar problemas, obter conselhos e aprender com as experiências de outras pessoas.")
@bot.message_handler(commands=["biblioteca"])
def biblioteca(mensagem):
    bot.send_message(mensagem.chat.id, "A biblioteca ou package utilizada, pyTelegramBotApi. Precisa-se baixar e instalar em um terminal, com os comandos pip install pytelegrambotapi. E em seguida utilizando o import telebot")


@bot.message_handler(commands=["1"])
def opcao1(mensagem):
    texto = """
    O que você quer? (Clique em uma opção)
/linguagem Linguagem
/biblioteca Bibliotecas
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Feedback para enviar sugestões, mande para este E-mail (emailaqui@gmail.com)")

@bot.message_handler(commands=["3"])
def opcao3(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "Informações de onde está o código fonte, neste link (github.com)")


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
/1 Explicando o Bot Api em Python
/2 Enviar um sugestões.
/3 Para mais informações.
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()
