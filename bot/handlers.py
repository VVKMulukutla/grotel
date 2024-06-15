from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler, CommandHandler, MessageHandler, Filters
from .api_client import fetch_data_from_groq

CHOOSE_MODEL, GET_INFERENCE = range(2)

def start(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Gemma-7b-it', 'Llama3-8b', 'Mixtral-8x7B', 'Llama3-70B']]
    update.message.reply_text(
        'Hello! I am your Groq Bot. Please choose a model to produce the inference:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return CHOOSE_MODEL

def choose_model(update: Update, context: CallbackContext) -> int:
    context.user_data['model'] = update.message.text
    update.message.reply_text(
        f'You have chosen {update.message.text}. Now please enter the input for the inference:'
    )
    return GET_INFERENCE

def get_inference(update: Update, context: CallbackContext) -> int:
    model = context.user_data['model']
    user_input = update.message.text
    try:
        response = fetch_data_from_groq(user_input, model)
        update.message.reply_text(f'Inference result from {model}: {response}')
    except Exception as e:
        update.message.reply_text(f'Error: {e}')
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Operation cancelled.')
    return ConversationHandler.END
