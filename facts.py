import pyperclip, random
from time import sleep

if __name__ == '__main__':
    with open("facts.txt", encoding='utf-8') as facts:
        fact_list = facts.read().split('\n')

        while True:
            i = random.randrange(0, len(fact_list) - 1)
            pyperclip.copy(fact_list[i])
            sleep(3)
