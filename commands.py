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

    /algoritmo_euclides <i>a b</i> - MCD( a , b )
    /algoritmo_ext_euclides <i>a b</i> - MCD( a , b ), además de u y v tales que au + bv = 1
    /congruencia_lineal <i>a b m</i> - Resuelve la congruencia lineal ax ≡ b (mod m)
    /ecuacion_diofantica <i>a b c</i> - Resuelve la ecuación diofántica ax + by = c
    """

    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, msg, parse_mode='HTML')

def cmd_algoritmo_euclides(update,context):
    msg = "El MCD ("+str(context.args[0])+" , "+str(context.args[1])+" ) = "+str(fn.alg_euclides(int(context.args[0]),int(context.args[1])))+"\n"
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, msg, parse_mode='HTML')

def cmd_algoritmo_ext_euclides(update,context):
    r,s,t = fn.alg_ext_euclides(int(context.args[0]),int(context.args[1]))
    msg = "El MCD ("+str(context.args[0])+" , "+str(context.args[1])+" ) =" + str(r) + "\n" + "u: " + str(s) + "\n" + "v: " + str(t) + "\n"
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, msg, parse_mode='HTML')

def cmd_congruencia_lineal(update,context):
    x, m = fn.congruencia_lineal(int(context.args[0]),int(context.args[1]),int(context.args[2]))
    if x == False:
        msg = "Esta congruencia no tiene solución"
    else:
        msg = "{El conjunto de todas las soluciones es x = " + str(x) + " + " + str(m) + "k, con k ∈ Z}\n"
        
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, msg, parse_mode='HTML')

def cmd_ecuacion_diofantica(update,context):
    msg = fn.ecuacion_diofantica(int(context.args[0]),int(context.args[1]),int(context.args[2]))
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, msg, parse_mode='HTML')
