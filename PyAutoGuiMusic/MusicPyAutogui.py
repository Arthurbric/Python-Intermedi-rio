import pyautogui
from time import sleep
import webbrowser


def search():
    original_string = pyautogui.prompt('Esta atras de qual musica ?')+" lyrics"
    new_separator = "+"

    split_list = original_string.split(' ')
    modified_string = new_separator.join(split_list)

    url = 'https://www.google.com/search?q=' + modified_string

    webbrowser.open(url)

def escrever(arq):
    sleep(2)
    pyautogui.press("win")
    pyautogui.write("note")
    sleep(1)
    pyautogui.press("enter")
    sleep(0.3)
    pyautogui.write(" ")
    for i in open(arq):
        pyautogui.write(i)
        pyautogui.press("enter")



while True:

    user_choice = pyautogui.confirm('Qual seria aopcao?', buttons=['Taylor swift','Outros'])

    if user_choice == 'Taylor swift':
        escrever('TaylorSwift.txt')

    else:
        search()
        sleep(10)


