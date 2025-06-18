from pynput.keyboard import Listener
def print(key):
  key = str(key)

with Listener(on_press=print) as listener:
  listener.join()
  print("key")