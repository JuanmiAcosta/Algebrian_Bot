import fn

def cmd_start(update,context):
    
    username = update.message.from_user.username
    if username is None:
        username = "usuario"
    
    msg = """\
    Hola {username}! Soy Algebrian_bot, tu asistente personal para ciertas funciones algebraicas, escribe "/help" para visualizar mis comandos.
    """

    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, msg.format(username=username))

def cmd_help(update,context):

    msg = """\
    Comandos disponibles:
    /start - Inicia el bot
    /help - Muestra mis comandos
    """

    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, msg)