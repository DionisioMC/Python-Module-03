import typing
import random


def gen_event() -> typing.Generator:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["swim", "use", "move", "release",
               "run", "grab", "climb", "eat", "sleep"]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(lst: list) -> typing.Generator:
    while len(lst) > 0:
        event = random.choice(lst)
        lst.remove(event)
        yield event


if __name__ == "__main__":
    generator = gen_event()
    for i in range(0, 1000):
        name, action = next(generator)
        print(f"Event {i}: Player {name} did action {action}")
    event_list = [next(generator) for i in range(10)]
    print(f"\nBuilt list of 10 events: {event_list}\n")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}\n")
