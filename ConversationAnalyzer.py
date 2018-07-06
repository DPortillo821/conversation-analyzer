from cmd import Cmd
from sys import argv

from QueryDefinitions.NumMessagesSent import NumMessagesSent

class ConversationAnalyzer(Cmd, NumMessagesSent):
    def __init__(self, args):
        super(ConversationAnalyzer, self).__init__()

    def do_quit(self, args):
        return True

if __name__ == '__main__':
    prompt = ConversationAnalyzer(argv[1])
    prompt.prompt = '>>> '
    prompt.cmdloop("Starting...\nType 'help' to get a list of possible queries to execute\nType 'quit' to quit the program ")