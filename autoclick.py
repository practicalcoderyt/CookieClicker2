from typing import List
from pynput import keyboard, mouse
# import time

STOP = False


def main():
    cursor = mouse.Controller()
    cursor.position = (400,900)

    listener = keyboard.Listener(on_press=on_keypress)
    listener.start()

    while not STOP:
        cursor.click(mouse.Button.left)
        # uncomment to ease click buffer
        #time.sleep(0.001)

    listener.stop()
    listener.join()

def on_keypress(key):
    global STOP
    STOP = True

if __name__ == '__main__':
    main()