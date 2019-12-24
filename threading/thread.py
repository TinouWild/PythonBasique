from threading import Thread
import time


def write_in_file(character):
    path = "demo.txt"
    with open(path, "a") as f:
        f.write(character)


class GetCharacter(Thread):
    def __init__(self, character):
        Thread.__init__(self)
        self.character = character

    def run(self):
        i = 0
        while i < 90000:
            write_in_file(self.character)
            i += 1


start = time.time()

thread_1 = GetCharacter('A')
thread_2 = GetCharacter('B')
thread_3 = GetCharacter('C')

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

print(str(time.time() - start) + " seconds")
