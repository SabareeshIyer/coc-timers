from timer_model import Timer
from typing import List
from datetime import datetime

FILENAME = "coc_running_upgrades.txt"

class FileAccess:
    def __init__(self):
        self.f = open(FILENAME, "r+")

    def prepare_content(self, timers):
        lines = []
        for timer in timers:
            line = timer.name + "~" + timer.endtime.strftime("%m/%d/%Y, %H:%M:%S") + "\n"
            lines.append(line)
        return lines

    def parse_file_contents(self, contents) -> List[Timer]:
        timers = []
        for line in contents:
            line = line.strip()
            name, endtimer = line.split("~")
            modified_endtimer = datetime.strptime(endtimer, "%m/%d/%Y, %H:%M:%S")
            timers.append(Timer(name, modified_endtimer))

        return timers

    def save_to_file(self, timers):
        self.clear_file_contents() # Clearing contents so we don't duplicate data.
        content = self.prepare_content(timers)
        self.f.writelines(content)


    def load_timers_from_file(self) -> List[Timer]:
        contents = self.f.readlines()
        return self.parse_file_contents(contents)

    def clear_file_contents(self):
        self.f.truncate(0)

    def __del__(self):
        self.f.close()

