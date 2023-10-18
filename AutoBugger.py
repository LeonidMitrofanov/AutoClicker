import pyautogui
from datetime import datetime
from pynput import keyboard


class AutoBugger:
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.01

    keyboard_listener = None

    # Время, когда нужно вывести текст (в формате ЧЧ:ММ:СС)
    timeToPress = datetime(2023, 10, 19, 00, 00, 00)


    # Массив для хранения позиций курсора мыши
    click_position = []

    def on_press(self, key):
        try:
            # Нажата клавиша
            print(f'[ {key.char} ]')

            if key.char == '`':
                self.click_position.clear()
                print('Все позиции курсора были удалены')


        except AttributeError:
            # Получаем текущую позицию курсора мыши и добавляем ее в массив
            print(f'[ {key} ]')
            if key == keyboard.Key.shift_l:
                current_position = pyautogui.position()
                self.click_position.append(current_position)
                print(f'Добавлена {len(self.click_position)}-я позиция курсора: {current_position}')
            # Удаляем последнюю записанную позицию курсора мыши из массива
            elif key == keyboard.Key.backspace:
                try:
                    pop_position = self.click_position.pop()
                    print(f'Удалена {len(self.click_position) + 1}-я позиция курсора: {pop_position}')
                except IndexError:
                    print(f'Список позиций курсора пуст')
            # Кликаем по позициям из массива self.click_position
            elif key == keyboard.Key.enter:

                while len(self.click_position) > 0:
                    current_time = datetime.now()
                    print(f"Осталось: {self.timeToPress-current_time}")
                    if current_time >= self.timeToPress:
                        print("Время для вывода текста!")
                        break
                for point in self.click_position:
                    pyautogui.click(point)
                    print(f"Click on {point}")

    def on_release(self, key):
        # print(f'Отпущена клавиша: {key}')
        if key == keyboard.Key.esc:
            # Прекращаем мониторинг клавиш и завершаем программу при нажатии клавиши Esc
            return False

    # Запускаем мониторинг клавиш
    def Start(self):
        # Создаем объект монитора клавиш
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.keyboard_listener.start()

    # Ждем, пока мониторинг клавиш не завершится
    def Stop(self):
        self.keyboard_listener.join()
