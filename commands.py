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

    <b>Aritmética entera modular</b>

    /congruencia_lineal <i>a b m</i> - Resuelve la congruencia lineal <i>ax ≡ b (mod m)</i>
    """

    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, msg, parse_mode='HTML')

def cmd_congruencia_lineal(update,context):
    