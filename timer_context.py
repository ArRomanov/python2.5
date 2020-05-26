import datetime
import time
import random


class TimerContext:
    def __init__(self):
        self.start_time = time.time()
        print(f"Время старта: {datetime.datetime.fromtimestamp(self.start_time).strftime('%H:%M:%S')}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish_time = time.time()
        print(f"Время завершение: {datetime.datetime.fromtimestamp(self.finish_time).strftime('%H:%M:%S')}")
        print(f"Общее время: {round(self.finish_time - self.start_time, 3)} секунд")

    def print_current_timer(self):
        current_timer = round(time.time() - self.start_time, 3)
        print(f'Текущее время: {current_timer} секунд')


if __name__ == '__main__':
    phrases = (
        'Расскажите про покупки! Про какие про покупки? Про покупки, про покупки, про покупочки свои',
        'Карл у Клары украл рекламу, а Клара у Карла украла бюджет',
        'Выборка по уборщицам на роллс-ройсах нерепрезентативна',
        'Кокосовары варят в скорококосоварках кокосовый сок'
    )

    print('Данная программа считает время набора на клавиатуре предложенного текста')
    while True:
        input('Если готовы, то просто нажмите Enter')
        chosen_phrase = phrases[random.randint(0, len(phrases) - 1)]
        with TimerContext() as timer:
            actual_phrase = input(f'{chosen_phrase}\n')
        try:
            assert chosen_phrase == actual_phrase
        except AssertionError:
            print('Вы допустили одну или несколько ошибок')
        do_resume = input('Еще раз? y/n\n')
        if do_resume == 'y':
            continue
        else:
            exit()
