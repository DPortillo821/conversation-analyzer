from cmd import Cmd

class ConversationAnalyzer(Cmd):
    """Simple command processor example."""

    def do_SHOW(self, args):
        print(args)
    
    def do_QUIT(self, args):
        return True

if __name__ == '__main__':
    prompt = ConversationAnalyzer()
    prompt.prompt = '>>> '
    prompt.cmdloop("Starting...\nType 'HELP' to get a list of possible queries to execute\nType 'QUIT' to quit the program ")