from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        with open('log.txt', 'a') as f:
            f.write(key.char)
    except AttributeError:
        print('special key {0} pressed'.format(key))

if __name__ == '__main__':
    l = keyboard.Listener(on_press=on_press)
    l.start()
    input()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
