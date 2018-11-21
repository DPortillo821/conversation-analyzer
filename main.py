from sys import argv

import pandas

from conversation_analyzer import ConversationAnalyzer

def main():
    # Under the section labeled "strftime() and strptime() Behavior" is a chart that has the meaning of each directive (%m, %d, %Y, etc)
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    date_parser = lambda x: pandas.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

    if (len(argv) is 1): # create data_frame from data found in ./conversation_files/sample_conversation.csv
        conversation_filename = './conversation_files/sample_conversation.csv'

        data_frame = pandas.read_csv(conversation_filename, parse_dates=['Date'], date_parser=date_parser)

        print(data_frame)
    elif (len(argv) is 2): # create data_frame from data found in given conversation file
        # TODO: validate second arg
        # Second arg should be the path to the desired conversation file as a csv (recommended to be located in the conversation_files directory)
        conversation_filename = argv[1]
        
        # TODO: catch failures for pandas.read_csv()
        data_frame = pandas.read_csv(conversation_filename, parse_dates=['Date'], date_parser=date_parser)
    else:
        # Too many args given
        print(f'ERROR: [{len(argv) - 1}] args found when exactly 1 is required')
        print('Required arg: path to the desired conversation file as a csv')
        return
    
    conversation_analyzer = ConversationAnalyzer(data_frame)

    prompt = conversation_analyzer
    prompt.intro = 'Starting...\nType "help" to get a list of possible queries to execute\nType "quit" to quit the program'
    prompt.ruler = '-'
    prompt.prompt = '>>> '

    try:
        prompt.cmdloop()
    except KeyboardInterrupt:
        print('\nQuitting...')

if __name__ == '__main__':
   main()
