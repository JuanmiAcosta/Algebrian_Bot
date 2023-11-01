import private
import commands
from telegram.ext import (Updater, CommandHandler)

def main():
    token = private.TOKEN
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    #EVENTOS QUE INICIARÁN EL BOT
    dp.add_handler(CommandHandler('start', commands.cmd_start))
    dp.add_handler(CommandHandler('help', commands.cmd_help))
    dp.add_handler(CommandHandler('algoritmo_euclides', commands.cmd_algoritmo_euclides))
    dp.add_handler(CommandHandler('algoritmo_ext_euclides', commands.cmd_algoritmo_ext_euclides))
    dp.add_handler(CommandHandler('congruencia_lineal', commands.cmd_congruencia_lineal))
    dp.add_handler(CommandHandler('ecuacion_diofantica', commands.cmd_ecuacion_diofantica))
    
    #INICIAMOS EL BOT
    updater.start_polling()
    #LISTENER
    updater.idle()



if __name__ == '__main__':
    print(f'Bot iniciado y listo para servir...')
    main()