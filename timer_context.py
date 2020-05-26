import datetime
import time


class TimerContext:
    def __init__(self):
        self.start_time = time.time()
        print(f"Время создания контекста: {datetime.datetime.fromtimestamp(self.start_time).strftime('%H:%M:%S')}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish_time = time.time()
        print(f"Время закрытия контекста: {datetime.datetime.fromtimestamp(self.finish_time).strftime('%H:%M:%S')}")
        print(f"Контекст работал: {round(self.finish_time - self.start_time, 3)} секунд")

    def print_current_timer(self):
        current_timer = round(time.time() - self.start_time, 3)
        print(f'Текущий таймер: {current_timer} секунд')


if __name__ == '__main__':
    with TimerContext() as timer:
        time.sleep(5)
        timer.print_current_timer()
        time.sleep(1)
        timer.print_current_timer()
        time.sleep(2)
        timer.print_current_timer()
