import pyautogui
import datetime as dt
import time
from pynput import keyboard

# Массив для хранения позиций курсора мыши
click_position = []


def on_press(key):
    try:
        # Нажата клавиша
        print(f'[ {key.char} ]')

        if key.char == '`':
            click_position.clear()
            print('Все позиции курсора были удалены')

    except AttributeError:
        # Получаем текущую позицию курсора мыши и добавляем ее в массив
        print(f'[ {key} ]')
        if key == keyboard.Key.shift_l:
            current_position = pyautogui.position()
            click_position.append(current_position)
            print(f'Добавлена {len(click_position)}-я позиция курсора: {current_position}')
        # Удаляем последнюю записанную позицию курсора мыши из массива
        elif key == keyboard.Key.backspace:
            try:
                pop_position = click_position.pop()
                print(f'Удалена {len(click_position) + 1}-я позиция курсора: {pop_position}')
            except IndexError:
                print(f'Список позиций курсора пуст')
        # Кликаем по позициям из массива click_position
        elif key == keyboard.Key.enter:
            for point in click_position:
                pyautogui.click(point)
                print(f"Click on {point}")


def on_release(key):
    # print(f'Отпущена клавиша: {key}')
    if key == keyboard.Key.esc:
        # Прекращаем мониторинг клавиш и завершаем программу при нажатии клавиши Esc
        return False


def main(name):
    pyautogui.FAILSAFE = True
    # Создаем объект монитора клавиш и запускаем мониторинг
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        print("Start program")
        # Ждем, пока мониторинг клавиш не завершится
        listener.join()
        print("Program complete")


if __name__ == '__main__':
    main('PyCharm')
