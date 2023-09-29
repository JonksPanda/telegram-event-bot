from ics import Calendar, Event

from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler


class Bot:

    def __init__(self, token) -> None:
        self.token = token
        self.app = ApplicationBuilder().token(self.token).build()
        test_handler = CommandHandler('test', self.com_test)
        newevent_handler = CommandHandler('newevent', self.com_newevent)

        self.app.add_handler(test_handler)
        self.app.add_handler(newevent_handler)

    def run_bot(self):
        self.app.run_polling()

    async def com_test(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="hello world!")

    # Handles logic behind newevent command
    async def com_newevent(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        # placeholder for now
        event_msg = """
        my event

        some description here bla bla bla

        time: 10/10 12:00:00

        place: stockholm
        """
        # responds to newevent with an .ics file
        await context.bot.send_message(chat_id=update.effective_chat.id, text=event_msg)
        await context.bot.send_document(chat_id=update.effective_chat.id, document=open(self.generate_ics(), "rb"))

    def generate_ics(self):
        calendar = Calendar()
        event = Event()
        event.name = "test"
        event.organizer = "test"
        event.begin = "2023-10-10 12:00:00"
        event.end = "2023-10-10 13:00:00"
        calendar.events.add(event)
        print(calendar.events)
        filepath = f"data/events/{event.name}.ics"
        with open(filepath, "w") as f:
            f.writelines(calendar.serialize_iter())
        return filepath
