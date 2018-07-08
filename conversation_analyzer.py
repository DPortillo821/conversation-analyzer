from cmd import Cmd
from datetime import datetime
from re import search

from query_definitions.numMessagesSent import NumMessagesSent

class ConversationAnalyzer(Cmd, NumMessagesSent, object):
    # TODO: Need to create more possible regex patterns and group them within a list. 
    # These will be used for verfication and to parse. Doing this work should go with updating the sample_conversation.txt file to include multi-line messages

    # TODO: This regex patterns needs to be more robust
    REGEX_PATTERN_2 = '([0-9]{1,2} [A-Z]{1}[a-z]+ [0-9]{4} at [0-9]{1,2}:[0-9]{2} [A-Z]{2}), ([A-Za-z0-9]+) : ([A-Za-z\\s\\W]+)'

    def __init__(self, conversation_file):
        super(ConversationAnalyzer, self).__init__()

        self.conversation_file = conversation_file
        self.conversation_dict = {}
        self.users = []

    def parse_conversation(self):
        line = self.conversation_file.readline()

        # line will be empty string when end-of-file (EOF) has been reached
        while (line != ''):
            # TODO: Verify that each line encountered falls into one of the regex patterns defined
            regex_groups = search(self.REGEX_PATTERN_2, line)

            date_at_time_datetime = datetime.strptime(regex_groups.group(1), '%d %B %Y at %I:%M %p')

            year = date_at_time_datetime.year
            month = date_at_time_datetime.month
            day = date_at_time_datetime.day
            hour = date_at_time_datetime.hour
            minute = date_at_time_datetime.minute
            user = regex_groups.group(2)
            message = regex_groups.group(3)

            # Keep track of all users seen
            if (user not in self.users):
                self.users.append(user)

            # Record this info into the conversation_dict
            self.record_message_into_year(year, month, day, hour, minute, user, message)

            # Grab next line to be parsed
            line = self.conversation_file.readline()

        # Uncomment this next line to see the entire conversation as a dict
        # print(self.conversation_dict)

    ### Query Methods

    def do_describe(self, args):
        print(self.users)

    def do_quit(self, args):
        print('Quitting...')
        self.conversation_file.close()
        return True

    ### Helper functions

    def record_message_into_year(self, year, month, day, hour, minute, user, message):
        if year in self.conversation_dict:
            # We've seen this year already! Continue recording the message into the month
            self.record_message_into_month(year, month, day, hour, minute, user, message)
        else:
            # First time this year has been seen! Record this year and continue recording the message into the month
            # TODO: There's a bit of inefficiency here. If we haven't seen the year then we definitely haven't seen the month, day, etc...
            self.conversation_dict[year] = {}
            self.record_message_into_month(year, month, day, hour, minute, user, message)

    def record_message_into_month(self, year, month, day, hour, minute, user, message):
        if month in self.conversation_dict[year]:
            # We've seen this month this year already! Continue recording the message into the day
            self.record_message_into_day(year, month, day, hour, minute, user, message)
        else:
            # First time this month has been seen this year! Record this month and continue recording the message into the day
            self.conversation_dict[year][month] = {}
            self.record_message_into_day(year, month, day, hour, minute, user, message)

    def record_message_into_day(self, year, month, day, hour, minute, user, message):
        if day in self.conversation_dict[year][month]:
            # We've seen this day this month already! Continue recording the message into the hour
            self.record_message_into_hour(year, month, day, hour, minute, user, message)
        else:
            # First time this day has been seen this month! Record this day and continue recording the message into the hour
            self.conversation_dict[year][month][day] = {}
            self.record_message_into_hour(year, month, day, hour, minute, user, message)

    def record_message_into_hour(self, year, month, day, hour, minute, user, message):
        if hour in self.conversation_dict[year][month][day]:
            # We've seen this hour this day already! Continue recording the message into the minute
            self.record_message_into_minute(year, month, day, hour, minute, user, message)
        else:
            # First time this hour has been seen this day! Record this hour and continue recording the message into the minute
            self.conversation_dict[year][month][day][hour] = {}
            self.record_message_into_minute(year, month, day, hour, minute, user, message)

    def record_message_into_minute(self, year, month, day, hour, minute, user, message):
        if minute in self.conversation_dict[year][month][day][hour]:
            # We've seen this minute this hour already! Continue recording the message into the user
            self.record_message_into_user(year, month, day, hour, minute, user, message)
        else:
            # First time this minute has been seen this hour! Record this new minute and continue recording the message into the user
            self.conversation_dict[year][month][day][hour][minute] = {}
            self.record_message_into_user(year, month, day, hour, minute, user, message)

    def record_message_into_user(self, year, month, day, hour, minute, user, message):
        if user in self.conversation_dict[year][month][day][hour][minute]:
            # We've seen this user this minute already! Continue recording their message into their list
            self.conversation_dict[year][month][day][hour][minute][user].append(message)
        else:
            # First time this user has been seen this minute! Record this new user and save their message into a new list
            self.conversation_dict[year][month][day][hour][minute][user] = [message]
