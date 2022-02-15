from timer_model import Timer
from datetime import datetime, timedelta
from file_handler import FileAccess

class Timers:
    def __init__(self):
        self.file = FileAccess()
        self.timers = self.file.load_timers_from_file()

    def add_timer(self, name, countdown_time):
        endtime = self.get_finish_time(countdown_time)
        timer = Timer(name, endtime)
        self.timers.append(timer)
        self.sort_timers()


    def sort_timers(self):
        self.timers.sort(key=lambda t: t.endtime)


    def get_finish_time(self, time):
        """Given the amount of time left in a timer, return the time at which this timer will run down"""
        d, h, m = time.split(' ')
        now = datetime.now()
        target = now + timedelta(days=int(d), hours=int(h), minutes=int(m))
        return target


    def clear_expired_timers(self):
        expired_timers = []
        for i, timer in enumerate(self.timers.copy()):
            if timer.endtime < datetime.now():
                expired_timers.append(timer)
                del self.timers[i]
            else:
                break

        if expired_timers:
            print(f"Expired timers:\n{expired_timers}")


    def print_timer(self, timer: Timer):
        delta = timer.endtime - datetime.now()
        print(f'Base: {timer.name}\tTime left: {(delta)}')


    def check_next_timer(self):
        if not self.timers:
            print("No active timers.")
            return

        self.clear_expired_timers()
        self.print_timer(self.timers[0])


    def show_all_timers(self):
        if not self.timers:
            print("No active timers.")
        for timer in self.timers:
            self.print_timer(timer)


    def delete_all_timers(self):
        self.timers = []
        self.file.clear_file_contents()


    def quit(self):
        self.file.save_to_file(self.timers)
        self.file.__del__() # close file on exit