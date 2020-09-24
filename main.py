#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards.
"""
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import var_TG
from var_TG import TOKEN

logging.basicConfig(filename="log.log",format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

info_uk_str = "Режим работы УК:\r\n" \
              "пн-чт: 09:00 - 18:00\r\n" \
              "пт до 17:00 \r\n" \
              "сб до 15:00\r\n" \
              "обед 13:00 - 13:45\r\n" \
              "Воскресенье - выходной\r\n" \
              "Бухгалтерия: \r\n" \
              "1 и 3 суббота рабочие, 2 и 4 выходной\r\n" \
              "Телефон УК: +7(495) 455-04-62\r\n" \
              "Дежурный:+7(499) 401-61-90\r\n" \
              "                    +7(495) 401-61-52"

bus29 = "От Станции:\r\n" \
        "06:19 06:59 07:39 08:04\r\n" \
        "08:19 08:44 08:59 09:24\r\n" \
        "10:04 10:39 11:19 11:59\r\n" \
        "12:14 12:39 12:54 13:34\r\n" \
        "14:19 14:59 15:19 15:39\r\n" \
        "15:59 16:39 17:19 17:59\r\n" \
        "18:19 18:43 19:04 19:54\r\n" \
        "20:36 21:15\r\n" \
        "От Володарского к станции:\r\n" \
        "06:19 06:59 07:39 08:04\r\n" \
        "08:19 08:44 08:59 09:24\r\n" \
        "10:04 10:39 11:19 11:59\r\n" \
        "12:14 12:39 12:54 13:34\r\n" \
        "14:19 14:59 15:19 15:39\r\n" \
        "15:59 16:39 17:19 17:59\r\n" \
        "18:19 18:43 19:04 19:54\r\n" \
        "20:36 21:15"

info_operation_str = "Участковый: \r\n" \
       "ПЧ Нахабино:      +7(495) 566-01-12 \r\n"\
       "Дежурная часть: +7 (495) 566-06-53\r\n" \
                     "                                " \
                     "+7 (495) 566-35-50\r\n"

def start(update, context):
    print("update = ", update)

    if update.effective_chat.type == "private":
        keyboard = [[InlineKeyboardButton("Выход", callback_data='exit'),
                 InlineKeyboardButton("В меню", callback_data='menu')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("Я вас категорически приветствую", reply_markup=reply_markup)



def menu(update, context):

    query = update.callback_query
    keyboard = [[InlineKeyboardButton("УК", callback_data='info_uk'),
                 InlineKeyboardButton("Расписание автобусов", callback_data='bus')],
                [InlineKeyboardButton("Мы в сети", callback_data='links')],
                [InlineKeyboardButton("Опреративные службы", callback_data='info_operation')],
                [InlineKeyboardButton("Предложения по улучшению бота", url='https://t.me/malina_it'),
                 InlineKeyboardButton("Выход", callback_data='exit')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Я ещё маленький бот и могу немного. Я знаю расписание работы и телефоны УК,"
                                 " могу подсказать расписание автобусов, адреса страничек в соцсетях "
                                 "и чатиков.", reply_markup=reply_markup)



def lic(update, context):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("Понял", callback_data='menu')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="не хами и не хамим будешь, \r\n"
                                 "не рекламируй ничего здесь и не будешь лишён голоса,\r\n"
                                 "не спамь и не забанен будешь", reply_markup=reply_markup)

def links(update, context):
    query = update.callback_query
    VK = [[InlineKeyboardButton("Открытая группа VK", url='https://vk.com/malina_nahabino'),
            InlineKeyboardButton("Закрытая группа VK", url='https://vk.com/dolwiki_malina')],
          [InlineKeyboardButton("Чат соседей WhatsApp", url='https://chat.whatsapp.com/JfhCcLqSxwbL9grweoEnOg'),
           InlineKeyboardButton("Остатки материалов WhatsApp", url='https://chat.whatsapp.com/FA53441zdgfJpp0ysXcK4q')],
          [InlineKeyboardButton("В меню", callback_data='menu'),
                 InlineKeyboardButton("Выход", callback_data='exit')]]

    reply_markup = InlineKeyboardMarkup(VK)
    query.edit_message_text(text="Ресурсы", reply_markup=reply_markup)

def info_operation(update, context):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("В меню", callback_data='menu'),
                 InlineKeyboardButton("Выход", callback_data='exit')],
                [InlineKeyboardButton("Сохранить и выйти", callback_data='save_operation')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=info_operation_str, reply_markup=reply_markup)

def info_uk(update, context):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("В меню", callback_data='menu'),
                 InlineKeyboardButton("Выход", callback_data='exit')],
                [InlineKeyboardButton("Сохранить и выйти", callback_data='save_uk')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=info_uk_str, reply_markup=reply_markup)

def bus(update, context):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("29", callback_data='bus1'),
                 InlineKeyboardButton("28", callback_data='bus2')],
                [InlineKeyboardButton("В меню", callback_data='menu'),
                 InlineKeyboardButton("Выход", callback_data='exit')]
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="выберите номер автобуса", reply_markup=reply_markup)

def bus1(update, context):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("Назад", callback_data='bus'),
                 InlineKeyboardButton("Выход", callback_data='exit')],
                [InlineKeyboardButton("Сохранить и выйти", callback_data='save_29')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=bus29, reply_markup=reply_markup)


def bus2(update, context):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("Назад", callback_data='bus'),
                 InlineKeyboardButton("Выход", callback_data='exit')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Великий нахабинский рандом!", reply_markup=reply_markup)

def exit(update, context):
    query = update.callback_query
    query.edit_message_text(text="До встречи".format(query.data))

def save_uk(update, context):
    query = update.callback_query
    query.edit_message_text(text=info_uk_str.format(query.data))

def save_operation(update, context):
    query = update.callback_query
    query.edit_message_text(text=info_operation_str.format(query.data))

def save_29(update, context):
    query = update.callback_query
    query.edit_message_text(text=bus29.format(query.data))

def button(update, context):
    query = update.callback_query
    if query.data == "menu":
        menu(update, context)
    elif query.data == "lic":
        lic(update, context)
    elif query.data == "info_operation":
        info_operation(update, context)
    elif query.data == "info_uk":
        info_uk(update, context)
    elif query.data == "bus":
        bus(update, context)
    elif query.data == "bus1":
        bus1(update, context)
    elif query.data == "bus2":
        bus2(update, context)
    elif query.data == "exit":
        exit(update, context)
    elif query.data == "save_uk":
        save_uk(update, context)
    elif query.data == "save_29":
        save_29(update, context)
    elif query.data == "save_operation":
        save_operation(update, context)
    elif query.data == "links":
        links(update, context)
    else:
        query.edit_message_text(text="нет нужного меню в обработчике".format(query.data))


def help(update, context):
        query = update.callback_query
        print("update = ", update)
        keyboard = [[InlineKeyboardButton("В меню", callback_data='menu'),
                     InlineKeyboardButton("Ознакомиться", callback_data='lic')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_user.id, text="Приветствую тебя, человек!\r\n"
                                                                        "Раз уж ты здесь предлагаю тебе ознакомиться"
                                                                        " с правилами нашего сообщества их не много,"
                                                                        " но всё же.\r\nМеня всегда можно вызвать "
                                                                        "командой /start", reply_markup=reply_markup)

    #context.bot.send_message ( chat_id=update.effective_user.id, text="Используйте  /start для начала работы с ботом.")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
