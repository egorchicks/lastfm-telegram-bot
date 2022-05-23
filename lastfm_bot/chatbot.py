from secret import TGTOKEN, LFTOKEN
from telegram.ext import Updater, CommandHandler
from lastfm_bot import get_recent, get_top, get_week, get_month, get_year

import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

updater = Updater(TGTOKEN)
dispatcher = updater.dispatcher

def start(update, context):
    logging.info(f'I am inside start handler from {update.effective_user}, {update.effective_chat}')
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text="""
        Hello, I'm LastFM telegram bot! write /help for help
        """
    )

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def help(update, context):
    logging.info(f'I am inside help handler from {update.effective_user}, {update.effective_chat}')
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text="""
Hello, I'm LastFM telegram bot, I can:
/start - to start bot
/help - to see the list of commands
/recent <your name> - to see your recent listenings
/week <your name> - to see your weekly top listenings
/month <your name> - to see your monthly top listenings
/year <your name> - to see your yearly top listenings
/top <your name> - to see your overall top listenings
/default <your name> - to set your account name as default
""".strip()
)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

def recent_tracks(update, context):
    logging.info(f'I am inside recent_tracks handler from {update.effective_user}, {update.effective_chat}')
    chat_id = update.effective_chat.id
    args = context.args
    user = ' '.join(args)
    if not user:
        user = context.user_data.get('user', 'Exzotics')
    context.bot.send_message(
        chat_id=chat_id,
        text=get_recent(user)
    )

recent_tracks_handler = CommandHandler('recent', recent_tracks)
dispatcher.add_handler(recent_tracks_handler)

def top_tracks(update, context):
    logging.info(f'I am inside top_tracks handler from {update.effective_user}, {update.effective_chat}')
    chat_id = update.effective_chat.id
    args = context.args
    user = ' '.join(args)
    if not user:
        user = context.user_data.get('user', 'Exzotics')
    context.bot.send_message(
        chat_id=chat_id,
        text=get_top(user)
    )

top_tracks_handler = CommandHandler('top', top_tracks)
dispatcher.add_handler(top_tracks_handler)

def week_tracks(update, context):
    logging.info(f'I am inside week_tracks handler from {update.effective_user}, {update.effective_chat}')
    chat_id = update.effective_chat.id
    args = context.args
    user = ' '.join(args)
    if not user:
        user = context.user_data.get('user', 'Exzotics')
    context.bot.send_message(
        chat_id=chat_id,
        text=get_week(user)
    )

week_tracks_handler = CommandHandler('week', week_tracks)
dispatcher.add_handler(week_tracks_handler)

def month_tracks(update, context):
    logging.info(f'I am inside week_tracks handler from {update.effective_user}, {update.effective_chat}')
    chat_id = update.effective_chat.id
    args = context.args
    user = ' '.join(args)
    if not user:
        user = context.user_data.get('user', 'Exzotics')
    context.bot.send_message(
        chat_id=chat_id,
        text=get_month(user)
    )

month_tracks_handler = CommandHandler('month', month_tracks)
dispatcher.add_handler(month_tracks_handler)

def year_tracks(update, context):
    logging.info(f'I am inside week_tracks handler from {update.effective_user}, {update.effective_chat}')
    chat_id = update.effective_chat.id
    args = context.args
    user = ' '.join(args)
    if not user:
        user = context.user_data.get('user', 'Exzotics')
    context.bot.send_message(
        chat_id=chat_id,
        text=get_year(user)
    )

year_tracks_handler = CommandHandler('year', year_tracks)
dispatcher.add_handler(year_tracks_handler)

def default(update, context):
    logging.info(f'I am inside default handler from {update.effective_user}, {update.effective_chat}')
    chat_id = update.effective_chat.id
    args = context.args
    context.user_data['user'] = ' '.join(args)
    user = ' '.join(args)
    context.bot.send_message(
        chat_id=chat_id,
        text=f'Successfully installed default user {user}'
    )

default_handler = CommandHandler('default', default)
dispatcher.add_handler(default_handler)

updater.start_polling()
updater.idle()