import json
from threading import Thread


def write_in_file():
    path = "demo.json"
    with open(path, "w") as f:
        json.dump(list(range(10)), f, indent=4)


class GetCharacter(Thread):
    def __init__(self, character):
        Thread.__init__(self)
        self.character = character

    def run(self):
        i = 0
        while i < 10000:
            write_in_file()
            i += 1


thread_1 = GetCharacter('A')
thread_2 = GetCharacter('B')
thread_3 = GetCharacter('C')

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()
