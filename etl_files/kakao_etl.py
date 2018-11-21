# transform file to only have one record per line
# seek lines that have the format Thursday, 30 May 2018 (this is an indicator that the next line is the beginning)
# read next line and grab datetime and user and partial content
# scan next line and see if there is a new line followed by a line that has the previously mentioned pattern
# if that's not the case then the next line is part of the content

from datetime import datetime
from re import match
from sys import argv

def transform():
    file_name = argv[1]

    input_file = open(file_name, 'r')

    REGEX_1 = r'(.+), (\d{1,2}) ([A-Za-z]+) (\d{4}\n)'
    REGEX_2 = u'([\d]{1,2} [A-Z]{1}[a-z]+ [\d]{4} at [\d]{1,2}:[\d]{2} [A-Z]{2}), ([A-Za-z\d\s\u3131-\ucb4c]+) : ([\dA-Za-z\:\s\W\u3131-\ucb4c]+)\n?'

    output_file = open(f'{file_name}.csv', 'w')

    line = input_file.readline()
    date_at_time_datetime = None
    user = ''
    message = ''
    while (line != ''):
        if (match(REGEX_1, line) != None):
            # Delete the last two \n and output then reset message
            if (message != ''):
                message = message.replace('\n', '\\n').replace('"', '\\"').replace('“', '\\"').replace('”', '\\"')
                output_file.write('{},{},"{}"\n'.format(date_at_time_datetime.strftime('%m.%d.%Y %H:%M:%S'), user, message))
                message = ''
        elif (match(REGEX_2, line) != None):
            if (message != ''):
                # Detete last \n
                message = message.replace('\n', '\\n').replace('"', '\\"').replace('“', '\\"').replace('”', '\\"')
                output_file.write('{},{},"{}"\n'.format(date_at_time_datetime.strftime('%m.%d.%Y %H:%M:%S'), user, message))
                regex_groups = match(REGEX_2, line)
                date_at_time_datetime = datetime.strptime(regex_groups.group(1), '%d %b %Y at %I:%M %p')
                user = regex_groups.group(2)
                message = regex_groups.group(3)
            else:
                regex_groups = match(REGEX_2, line)
                date_at_time_datetime = datetime.strptime(regex_groups.group(1), '%d %b %Y at %I:%M %p')
                user = regex_groups.group(2)
                message = regex_groups.group(3)
        elif (line == '\n'):
            message = message + '\n'
        else:
            message = message + line

        # Read next line
        line = input_file.readline()

    input_file.close()
    output_file.close()

if __name__ == '__main__':
    transform()
