from cmd import Cmd

from query_definitions.numMessagesSent import NumMessagesSent

class ConversationAnalyzer(Cmd, NumMessagesSent, object):
    def __init__(self, data_frame):
        super(ConversationAnalyzer, self).__init__()

        self.data_frame = data_frame

    ### Query Methods

    def do_describe(self, args):
        pass

    def do_quit(self, args):
        print('Quitting...')
        return True
