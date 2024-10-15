import time
import datetime
from playsound import playsound


def log(txt):
    """
    Записывает текстовое сообщение в лог-файл с временной меткой.

    Параметры:
    txt (str): Сообщение для записи в лог.
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} - {txt}\n"

    try:
        with open("log_gm.txt", "a") as file:  # append mode
            file.write(log_entry)
    except Exception as e:
        print(f"Ошибка при записи в лог: {e}")

    print(txt)  # По-прежнему выводим сообщение в консоль


def timer(sec: int, message=None, sound_file=None):
    """
    Запускает таймер на указанное количество секунд.

    Параметры:
    sec (int): Количество секунд для отсчета.
    message (str): Сообщение, выводимое по завершении таймера. По умолчанию None.
    sound_file (str, optional): Путь к звуковому файлу, который будет воспроизведен по окончании таймера.
                                 Если None, звук не воспроизводится.

    Пример использования:
    timer(5, "Время вышло!", 'path/to/sound.mp3')
    """
    while sec >= 0:
        print(f'wait: {sec} sec.   ', end='\r')
        time.sleep(1)
        sec -= 1

    if sound_file:
        playsound(sound_file)
    if message:  # Воспроизводим звук, если файл указан
        print(message)  # Выводим сообщение по завершении таймера


# Пример использования
# Замените на путь к звуковому файлу
# timer(5, "Ваше сообщение!", 'path/to/sound.mp3')
