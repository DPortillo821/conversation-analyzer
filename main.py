from sys import argv

import pandas

from conversation_analyzer import ConversationAnalyzer

def main():
    headers = ['datetime', 'user', 'content']

    # Under the section labeled "strftime() and strptime() Behavior" is a chart that has the meaning of each directive (%m, %d, %Y, etc)
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    date_parser = lambda x: pandas.datetime.strptime(x, '%m.%d.%Y %H:%M:%S')

    if (len(argv) is 1):
        conversation_filename = './conversation_files/sample_conversation.csv'

        data_frame = pandas.read_csv(conversation_filename, names=headers, parse_dates=['datetime'], date_parser=date_parser)
    elif (len(argv) is 2):
        # TODO: validate arg.
        # First arg must be the name of the csv file that is to be analyzed (recommended to be located in the conversation-files directory)
        conversation_filename = argv[1]
        
        data_frame = pandas.read_csv(conversation_filename, names=headers, parse_dates=['datetime'], date_parser=date_parser)
    else:
        # TODO: Instruct that exactly two args should be passed; txt file and etl
        return
    
    conversation_analyzer = ConversationAnalyzer(data_frame)

    prompt = conversation_analyzer
    prompt.intro = 'Starting...\nType "help" to get a list of possible queries to execute\nType "quit" to quit the program'
    prompt.ruler = '-'
    prompt.prompt = '>>> '
    prompt.cmdloop()

if __name__ == '__main__':
   main()
