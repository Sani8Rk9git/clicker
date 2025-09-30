import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char='t')
clicking = False

mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.01)

def Toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking


#the main thread is listening for the toggle key
# another thread to run concurrently to do the actual clicking

click_Thread = threading.Thread(target=clicker)
click_Thread.start()

with Listener(on_press=Toggle_event) as listener:
    listener.join()