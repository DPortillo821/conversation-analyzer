from sys import argv

from conversation_analyzer import ConversationAnalyzer

def main():
    # TODO: validate number of args. Must be exactly one. Must be a txt file.
    conversation_file = open(argv[1], 'r')
    conversation_analyzer = ConversationAnalyzer(conversation_file)
    conversation_analyzer.parse_conversation()
    prompt = conversation_analyzer
    prompt.prompt = '>>> '
    prompt.cmdloop("Starting...\nType 'help' to get a list of possible queries to execute\nType 'quit' to quit the program ")

if __name__ == '__main__':
   main()