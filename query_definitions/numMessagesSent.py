from datetime import datetime
from re import search

class NumMessagesSent:
    def __init__(self, child):
        self.data_frame = child.data_frame

    def do_numMessagesSent(self, args):
        # Ex: BY user1 FROM 05.30.2018 @ 07:00 TO 06.01.2018 @ 08:00
        REGEX = 'BY ([A-Za-z0-9\s\u3131-\ucb4c]+) FROM ([0-9]{2}.[0-9]{2}.[0-9]{4} @ [0-9]{2}:[0-9]{2}) TO ([0-9]{2}.[0-9]{2}.[0-9]{4} @ [0-9]{2}:[0-9]{2})'

        regex_groups = search(REGEX, args)

        user = regex_groups.group(1)

        # Under the section labeled "strftime() and strptime() Behavior" is a chart that has the meaning of each directive (%m, %d, %Y, etc)
        # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
        start_datetime = datetime.strptime(regex_groups.group(2), '%m.%d.%Y @ %H:%M')
        end_datetime = datetime.strptime(regex_groups.group(3), '%m.%d.%Y @ %H:%M')

        print(self.data_frame[
                (self.data_frame['datetime'] >= start_datetime) & 
                (self.data_frame['datetime'] <= end_datetime) & 
                (self.data_frame.user == user)
        ].shape[0])
