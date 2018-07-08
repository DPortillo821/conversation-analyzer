class NumMessagesSent:
    def __init__(self, child):
        self.conversation_dict = child.conversation_dict
        self.users = child.users

    def do_numMessagesSent(self, args):
        count = 0

        for month_dict in self.conversation_dict.values():
            for day_dict in month_dict.values():
                for hour_dict in day_dict.values():
                    for minute_dict in hour_dict.values():
                        for user_list in minute_dict.values():
                            for user in user_list:
                                if (user == args):
                                    count += len(user_list[user])
        
        print(count)
