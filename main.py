import bot
import message
from ics import Calendar, Event


# const of project directory
DIR = None


def main():

    # Temporary calendar-file creation for testing purposes
    calendar = Calendar()
    event = Event()
    event.name = "test"
    event.begin = "2023-10-10 12:00:00"
    event.end = "2023-10-10 13:00:00"
    calendar.events.add(event)
    print(calendar.events)
    with open(f"data/events/{event.name}.ics", "w") as f:
        f.writelines(calendar.serialize_iter())


if __name__ == "__main__":
    main()
