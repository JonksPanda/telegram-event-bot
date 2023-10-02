from bot import Bot
from setup import Config

import logging


# const of project directory
DIR = None


def main():

    # Add ability to put token as argument

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, encoding="utf-8", filename=f"./data/logs/event_log.log")
    conf = Config()
    chat_bot = Bot(conf.credentials['token'])
    chat_bot.run_bot()


if __name__ == "__main__":
    main()
