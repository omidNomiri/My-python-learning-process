class Time:
    def __init__(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s
        self.fix()

    def sum(self, other):
        h_new = self.hours + other.hours
        m_new = self.minutes + other.minutes
        s_new = self.seconds + other.seconds
        return Time(h_new, m_new, s_new)

    def minus(self, other):
        h_new = self.hours - other.hours
        m_new = self.minutes - other.minutes
        s_new = self.seconds - other.seconds
        return Time(h_new, m_new, s_new)

    @classmethod
    def seconds_to_time(cls, s):
        hours = s // 3600
        minutes = (s % 3600) // 60
        seconds = (s % 3600) % 60
        return cls(hours, minutes, seconds)

    def time_to_seconds(self):
        return self.seconds + 60 * self.minutes + 3600 * self.hours

    def fix(self):
        while True:
            if self.seconds >= 60:
                self.seconds -= 60
                self.minutes += 1

            if self.minutes >= 60:
                self.minutes -= 60
                self.hours += 1
            
            if self.seconds < 0:
                self.minutes -= 1
                self.seconds +=60
            
            if self.minutes < 0:
                self.hours -= 1
                self.minutes += 60

            break

    def show(self):
        print(f"{self.hours}:{self.minutes}:{self.seconds}")
