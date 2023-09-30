from bot import Bot

import logging


# const of project directory
DIR = None


def main():

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, encoding="utf-8", filename=f"data/logs/event_log.log")

    with open("config/token.txt") as f:
        token = f.read()
    print(token)
    chat_bot = Bot(token)
    chat_bot.run_bot()


if __name__ == "__main__":
    main()
