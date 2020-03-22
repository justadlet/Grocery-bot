import telegram
import logging
import time
import os

from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, ConversationHandler, CallbackQueryHandler, CallbackContext
from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from config import bot_messages, bot_states, menu
from functools import wraps


# DB_Host = os.environ['DB_Host']
# DB_Database = os.environ['DB_Database']
# DB_User = os.environ['DB_User']
# DB_Port = os.environ['DB_Port']
# DB_Password = os.environ['DB_Password']

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level = logging.INFO)
                     
logger = logging.getLogger(__name__)
LIST_OF_ADMINS = [251961384]
custom_keyboard = [['/add', '/delete'],
                   ['/set', '/stop'],
                   ['/clear', '/showtasks'],
                   ['/feedback', '/help'],
                   ['/admin_help']]
reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard = True)
def log_text(debug_text):
  print(debug_text)

def send_message(context, chat_id, text):
    try:
        context.bot.send_message(chat_id = chat_id, text = text, parse_mode = "Markdown", reply_markup = reply_markup)
    except:
        log_text('No such chat_id using a bot')

def send_message_keyboard(context, chat_id, text, kbrd):
    try:
        context.bot.send_message(chat_id = chat_id, text = text, parse_mode = "Markdown", reply_markup = kbrd)
    except:
        log_text('No such chat_id using a bot')


def feedback(update, context):
    if not context.args:
        context.bot.send_message(chat_id = update.message.chat_id, text = bot_messages.feedback_write_text,  reply_markup = reply_markup)
        return bot_states.READ_FEEDBACK
    text = context.args[0]
    ith = 0
    for word in context.args:
        ith = ith + 1
        if ith > 1:
            text = text + " " + word
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    text = "❗️Хей, пользоветель бота отправил новый фидбэк всем админам: ❗️\n\nFeedback:\n" + text + "\n\nUsername: @" + str(username) + "\n\nUser ID: " + str(user_id)
    for admin_id in LIST_OF_ADMINS:
        context.bot.send_message(chat_id = admin_id, text = text)
    context.bot.send_message(chat_id = update.message.chat_id, text = bot_messages.feedback_success_command_response, reply_markup = reply_markup)

def read_feedback(update, context):
    text = update.message.text
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    text =  "❗️Хей, пользоветель бота отправил новый фидбэк всем админам: ❗️\n\nFeedback:\n" + text + "\n\nUsername: @" + str(username) + "\n\nUser ID: " + str(user_id)
    for admin_id in LIST_OF_ADMINS:
        context.bot.send_message(chat_id = admin_id, text = text)
    context.bot.send_message(chat_id = update.message.chat_id, text = bot_messages.feedback_success_command_response, reply_markup = reply_markup)
    return ConversationHandler.END

def get_base_inline_keyboard():
    keyboard = [
        # Каждый элемент внутри списка -- это один вертикальный столбец.
        # Сколько кнопок -- столько столбцов
        [
            InlineKeyboardButton('Овощи', callback_data = 'vegetables'),
            InlineKeyboardButton('Фрукты', callback_data = 'fruits'),
        ],
        [
            InlineKeyboardButton('Продукты', callback_data = 'meals'),
            InlineKeyboardButton('Напитки', callback_data = 'derinks'),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

def get_keyboard2(call_data):
    if call_data == "vegetables":
        keyboard = []
        whole_menu = menu.vegetables
        ith = 0
        for i in whole_menu:
            ith = ith + 1
            keyboard.append(InlineKeyboardButton(i, callback_data = str(ith)))
    elif call_data == "fruits":
        keyboard = []
        whole_menu = menu.fruits
        ith = 0
        for i in whole_menu:
            ith = ith + 1
            keyboard.append(InlineKeyboardButton(i, callback_data = str(ith)))
    elif call_data == "meals":
        keyboard = []
        whole_menu = menu.meals
        ith = 0
        for i in whole_menu:
            ith = ith + 1
            keyboard.append(InlineKeyboardButton(i, callback_data = str(ith)))
    elif call_data == "derinks":
        keyboard = []
        whole_menu = menu.derinks
        ith = 0
        for i in whole_menu:
            ith = ith + 1
            keyboard.append(InlineKeyboardButton(i, callback_data = str(ith)))
    keyboard.append(InlineKeyboardButton("Назад", callback_data = "back"))

    return InlineKeyboardMarkup(build_menu(keyboard, n_cols = 1))

def show_menu(update, context):
    user_id = update.effective_user.id
    reply_keyboard = get_base_inline_keyboard()
    send_message_keyboard(context, user_id, bot_messages.show_menu_text, reply_keyboard)
    return bot_states.CHECK_MENU

def check_show_menu(update, context):
    user_id = update.effective_user.id
    query = update.callback_query
    data = query.data
    current_text = update.effective_message.text
    kbrd = [
        [
            InlineKeyboardButton('Mesh', callback_data = 'vegetables'),
            InlineKeyboardButton('mesh', callback_data = 'fruits'),
        ]
    ]
    if data == "vegetables":
        query.edit_message_text(
            text = current_text,
            reply_markup = get_keyboard2("vegetables")
        )
    elif data == "fruits":
        query.edit_message_text(
            text = current_text,
            reply_markup = get_keyboard2("fruits")
        )      
    elif data == "meals":
        query.edit_message_text(
            text = current_text,
            reply_markup=get_keyboard2("meals")
        )            
    elif data == 'derinks':
        query.edit_message_text(
            text = current_text,
            reply_markup = get_keyboard2("derinks")
        )          
    elif data == "back" :
        query.edit_message_text(
            text = current_text,
            reply_markup = get_base_inline_keyboard()
        )
    return bot_states.CHECK_MENU

def start(update, context):
    context.bot.send_message(chat_id = update.message.chat_id, text = bot_messages.start_command_response, reply_markup = reply_markup)

def help(update, context):
    context.bot.send_message(chat_id = update.message.chat_id, text = bot_messages.help_command_response, reply_markup = reply_markup)

def unknown(update, context):
    context.bot.send_message(chat_id = update.message.chat_id, text = bot_messages.unknown_command_response, reply_markup = reply_markup)

def cancel(update, context):
    context.bot.send_message(chat_id = update.message.chat_id, text = bot_messages.cancelled_successfully, reply_markup = reply_markup)
    return ConversationHandler.END

def main():
    updater = Updater(token = "1130609306:AAFFWpVoazrjy0DYd4TrvEd2cLbfwE4_3EE", use_context = True)
    dp = updater.dispatcher
    feedback_handler = CommandHandler('feedback', feedback, pass_args = True, pass_chat_data = True)
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    unknown_handler = MessageHandler(Filters.command, unknown)
    show_menu_conv_handler = ConversationHandler(
        entry_points = [CommandHandler('show_menu', show_menu)],
        states = {
            bot_states.CHECK_MENU: [CallbackQueryHandler(check_show_menu)]
        },
        fallbacks = [CommandHandler('cancel', cancel)]
    )

    dp.add_handler(show_menu_conv_handler)
    dp.add_handler(feedback_handler)
    dp.add_handler(start_handler)
    dp.add_handler(help_handler)
    dp.add_handler(unknown_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()