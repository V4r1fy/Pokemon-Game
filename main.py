import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.name
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Hello {name}, How are you?')

if __name__ == '__main__':
    application = ApplicationBuilder().token('5965990822:AAFuYx1D29gy2v7MHLSxMVgSYoei9WS5PSw').build()

    hello_handler = CommandHandler('hello', hello)
    application.add_handler(hello_handler)

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()

