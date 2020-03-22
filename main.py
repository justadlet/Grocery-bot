import telegram
import logging
import time
import os

from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, ConversationHandler, CallbackQueryHandler , CallbackContext
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
    """ Получить клавиатуру для сообщения
        Эта клавиатура будет видна под каждым сообщением, где её прикрепили
    """
    
    keyboard = [
        # Каждый элемент внутри списка -- это один вертикальный столбец.
        # Сколько кнопок -- столько столбцов
        [
            InlineKeyboardButton('овощи', callback_data= 'vegetables'),
            InlineKeyboardButton('фрукты', callback_data= 'fruits'),
        ],
        [
            InlineKeyboardButton('продукты', callback_data='meals'),
            InlineKeyboardButton('напитки', callback_data='derinks'),
        ]
       
    ]
    return InlineKeyboardMarkup(keyboard)

    
    '''user_id = update.message.from_user.id
    whole_menu = bot_messages.menu_initial
    it = 1
    for i in list:
        new_list = str(it) + ". " + str(i)
        whole_menu = whole_menu + new_list + "\n"
        it = it + 1
    send_message(context, user_id, whole_menu)'''
    
 

def get_keyboard2(call_data):
    """ Получить вторую страницу клавиатуры для сообщений
        Возможно получить только при нажатии кнопки на первой клавиатуре
    """
   if call_data == "vegetables":
        keyboard = []
        menu = menu.vegetables
        
        
        ith = 0
        for i in menu:
            ith += 1
            keyboard.append(InlineKeyboardButton(i[0], callback_data = 'v' + str(ith)))
    
    elif call_data == "fruits":
        keyboard = []
        menu = menu.fruits
        
        
        ith = 0
        for i in menu:
            ith += 1
            keyboard.append(InlineKeyboardButton(i[0], callback_data = 'f' + str(ith)))
        
        
    elif call_data == "meals":
        keyboard = []
        menu = menu.meals
        
        
        ith = 0
        for i in menu:
            ith += 1
            keyboard.append(InlineKeyboardButton(i[0], callback_data = 'm' + str(ith)))

    elif call_data == "derinks":
        keyboard = []
        menu = menu.derinks
        
        
        ith = 0
        for i in menu:
            ith += 1
            keyboard.append(InlineKeyboardButton(i[0], callback_data = 'd' + str(ith)))
    
    keyboard.append(InlineKeyboardButton("назад", callback_data = 'back'))
    return InlineKeyboardMarkup(keyboard)    

def keyboard_callback_handler(update: Update, context: CallbackContext):
    """ Обработчик ВСЕХ кнопок со ВСЕХ клавиатур
    """
    query = update.callback_query
    data = query.data
    

    # Обратите внимание: используется `effective_message`
    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text
    
    if data == 'vegetables':
        # Показать следующий экран клавиатуры
        # (оставить тот же текст, но указать другой массив кнопок)
        query.edit_message_text(
            text=current_text,
            reply_markup=get_keyboard2('vegetables'),
        )
    elif data == 'fruits':
        # Показать следующий экран клавиатуры
        # (оставить тот же текст, но указать другой массив кнопок)
        query.edit_message_text(
            text=current_text,
            reply_markup=get_keyboard2('fruits'),
        )      
        
    elif data == 'meals':
        # Показать следующий экран клавиатуры
        # (оставить тот же текст, но указать другой массив кнопок)
        query.edit_message_text(
            text=current_text,
            reply_markup=get_keyboard2('meals'),
        )            
 
    elif data == 'derinks':
        # Показать следующий экран клавиатуры
        # (оставить тот же текст, но указать другой массив кнопок)
        query.edit_message_text(
            text=current_text,
            reply_markup=get_keyboard2('derinks'),
        )          
    elif data == 'back' :
        # Показать предыдущий экран клавиатуры
        # (оставить тот же текст, но указать другой массив кнопок)
        query.edit_message_text(
            text=current_text,
            reply_markup=get_base_inline_keyboard(),
        )    
    
    
    
    
    


    

def start(update, context):
    context.bot.send_message(chat_id = update.message.chat_id, text = bot_messages.start_command_response, reply_markup = reply_markup)

def help(update, context):
    context.bot.send_message(chat_id = update.message.chat_id, text = bot_messages.help_command_response, reply_markup = reply_markup)

def unknown(update, context):
    context.bot.send_message(chat_id = update.message.chat_id, text = bot_messages.unknown_command_response, reply_markup = reply_markup)

def main():
    updater = Updater(token = "1130609306:AAFFWpVoazrjy0DYd4TrvEd2cLbfwE4_3EE", use_context = True)
    dp = updater.dispatcher
    feedback_handler = CommandHandler('feedback', feedback, pass_args = True, pass_chat_data = True)
    show_menu_handler = CommandHandler('show_menu', show_menu)
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    unknown_handler = MessageHandler(Filters.command, unknown)

    dp.add_handler(show_menu_handler)
    dp.add_handler(feedback_handler)
    dp.add_handler(start_handler)
    dp.add_handler(help_handler)
    dp.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
