# Import the relevant modules
import pyautogui
import time

# To write something
secs_between_keys =0.04
pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)  # useful for entering text, newline is Enter

# Keyboard hotkeys like hotkey():
pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste
# - 'a', 'b', 'c', ..., 'z'
# - '0', '1', '2', ..., '9'
# - 'shift', 'ctrl', 'alt', 'win' (Windows key), 'esc'
# - 'left', 'right', 'up', 'down'
# - 'space', 'enter', 'tab', 'backspace'
# - 'delete', 'insert', 'home', 'end', 'pageup', 'pagedown'
# - 'f1', 'f2', ..., 'f12'

# - '+': Plus key (e.g., 'ctrl' + '+')
# - '-': Minus key (e.g., 'ctrl' + '-')
# - '*': Asterisk key (e.g., 'ctrl' + '*')
# - '/': Slash key (e.g., 'ctrl' + '/')
# - ',': Comma key
# - '.': Period key

# Individual button down and up events can be called separately:
"""
pyautogui.keyDown(key_name)
pyautogui.keyUp(key_name)
"""


# Message Box

pyautogui.alert('This displays some text with an OK button.')

pyautogui.confirm('This displays text and has an OK and Cancel button.')
# 'OK'
pyautogui.prompt('This lets the user type in a string and press OK.')


import pyautogui

# Display
user_choice = pyautogui.confirm('Quem e legal?', buttons=['Arthur', 'Kaynan','Os monitores'])

# Escolha
if user_choice == 'Arthur':
    choice = 'Arthur Arash'
elif user_choice == 'Kaynan':
    choice = 'Kaynan'
else:
    choice = 'os monitores'

pyautogui.alert(f'o {choice} e legal mesmo')

# Give the python file some time before continuing
time.sleep(3)

# Mouse Functions
# Prints the resolution of your screen
print(pyautogui.size())
# Prints the current position of the mouse
print(pyautogui.position())
# Moves the mouse over time (3 seconds)
pyautogui.moveTo(100, 100, 3)
# Move the mouse relative to its current position
pyautogui.moveRel(100, 100, 3)

# Drag
x,y,num_seconds = 100,100,3
xOffset,yOffset= 100, 100
pyautogui.dragTo(x, y, duration=num_seconds,button='left')  # drag mouse to XY
pyautogui.dragRel(xOffset, yOffset, duration=num_seconds,button='left')  # drag mouse relative to its current position

# Click
# .click(500, 500, how many time click , time, button="right/left/middle") es o mais completo
pyautogui.click(500, 500, clicks=2, interval=0.5, button='middle')
pyautogui.tripleClick()
pyautogui.doubleClick()
pyautogui.leftClick()
pyautogui.rightClick()

# Scrolls up 500
pyautogui.scroll(500)
# Scrolls down 500
pyautogui.scroll(-500)

# Mouse up and down
pyautogui.mouseUp(100, 100, button="left")
pyautogui.mouseDown(100, 100, button="left")

# Example of mouse up and down
pyautogui.mouseDown(300, 400, button="left")
pyautogui.moveTo(800, 400, 3)
pyautogui.mouseUp()
pyautogui.moveTo(1000, 400, 3)

# Intermittent drawing of lines on paint - NOT MENTIONED IN YOUTUBE VIDEO
time.sleep(3)
pyautogui.mouseDown(300, 400, button='left')
pyautogui.moveTo(500, 400)
pyautogui.mouseUp()
pyautogui.moveTo(700, 400)
pyautogui.mouseDown()
pyautogui.moveTo(900, 400)


# Spiral drawing using pyautogui
time.sleep(1)
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, distance, 1, button="left")
    pyautogui.dragRel(-distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, -distance, 1, button="left")
    time.sleep(4)


# TikTok Liker - example
time.sleep(3)
# range will be the number of TikTok's you want to like
for i in range(10):
    pyautogui.moveTo(450, 500)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.moveTo(854, 515)
    time.sleep(1)
    pyautogui.leftClick()


# Keyboard functions
pyautogui.write("hello")
pyautogui.press("enter")
pyautogui.press("space")
pyautogui.press("win") #para abrir windows
pyautogui.press("backspace") #PAra apagar

# Dino Game - Chrome
time.sleep(3)
for i in range(20):
    pyautogui.press("space")
    time.sleep(0.5)

# Screenshot in pyautogui
pyautogui.screenshot("screenshot.png")

# Example of hotKeys Ctr + C

pyautogui.keyDown('ctrl')
pyautogui.press('c')
pyautogui.keyUp('ctrl')


# Find an image
pyautogui.locateCenterOnScreen('looksLikeThis.png')  # returns center x and y

# Cheat Sheet -> https://pyautogui.readthedocs.io/en/latest/quickstart.html
#
