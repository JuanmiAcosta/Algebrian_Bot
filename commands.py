import fn

def cmd_start(update,context):
    
    username = update.message.from_user.username
    if username is None:
        username = "usuario"
    
    msg = """\
    Hola {username}! Soy Carbur_bot, tu asistente personal para el precio del carburante en tu zona, haz "/help" para visualizar mis comandos.
    """

    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, msg.format(username=username))

def cmd_help(update,context):

    msg = """\
    Comandos disponibles:
    /start - Inicia el bot
    /help - Muestra esta ayuda
    """

    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, msg)