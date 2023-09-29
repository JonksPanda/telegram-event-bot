from ics import Calendar, Event
import logging

from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler


class Bot:

    def __init__(self, token) -> None:
        self.token = token
        self.app = ApplicationBuilder().token(self.token).build()
        start_handler = CommandHandler('test', self.com_test)
        self.app.add_handler(start_handler)

    def run_bot(self):
        self.app.run_polling()

    async def com_test(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="hello world!")

    # def newEvent(self):
    #     pass
