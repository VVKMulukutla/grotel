from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from .config import TELEGRAM_BOT_TOKEN
from .handlers import start, choose_model, get_inference, cancel, CHOOSE_MODEL, GET_INFERENCE

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSE_MODEL: [MessageHandler(Filters.text & ~Filters.command, choose_model)],
            GET_INFERENCE: [MessageHandler(Filters.text & ~Filters.command, get_inference)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
