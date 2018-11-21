# conversation-analyzer
## Overview
The purpose of this program is to do analysis on any given conversation between two users.
(NOTE: we hope to add multiple user functionality in the future) 
The program extracts information from the conversation that can then be queried once run. 
Refer to sections [How to Use](#how-to-use) and [Query-Definitions and Query-Instances](#query-definitions-and-query-instances) for more details as to what type of queries can be asked and how they need to be asked as well as examples for each.

### Input
The input for this program is a csv file that represents a conversation.
There is a well-defined format that the conversation must be in. If the conversation does not adhere to the format then it will need to be transformed.
For this reason, there are different types of ETL tranformation files that can help with the transformation. These can be found within the [etl_files](etl_files) directory.
If there is no ETL that can transform the file then a new one will have to be created.
The conversation should have the general structure that, for a given message there is, at minimum, a date, time, and user associated with it. 

An example can be found in the [conversation_files](conversation_files) directory; [sample_conversation.csv](conversation_files/sample_conversation.csv)
Here is what is contained in that file:
```
Date,User,Message
2018-05-30 07:00:00,"user1","hey!"
2018-05-31 07:14:00,"user2","what's up?"
2018-06-01 07:47:00,"user1","how are you?"
2018-06-01 08:00:00,"user2","I'm good.

You?"
2018-06-02 08:14:00,"user1","Good as well"
2018-07-01 13:00:00,"user2","안녕"
```

Note the format of the date and time (YYYY-MM-DD HH:MM:SS) as well as the `"` around the User and the Message.
Messages can span multiple lines.

### Output
The output of a `Query` depends on which `Query` was run. 
For example, you could run a `Query` that asks “How many messages did user1 send on May 31st 2018?”  and the expected output should be a positive integer.

A different `Query` can ask “How long, on average, did it take user1 to reply for messages sent on dateX in minutes?” and the expected output should be a positive number in minutes.

## Getting started
### Installation requirements
For best results, it's recommended that you use a virtual environment when running this application and have python3.6 installed.

Install all requirements found in [requirements.txt](requirements.txt)
```bash
pip install -r ./requirements.txt
```

### How to run
You can start the program by running the following command within the command line:
```bash
python3 ./main.py ./conversation-files/{conversation}.csv
```
Where `{conversation}` refers to the name of the csv file which contains the conversation. Be sure the format of the conversation follows the same patterns described in the [Input](#input) section.

If you want to just play around with some sample data you can just execute
```bash
python3 ./main.py
```

### How to use
Once the program has started you will see `>>>` which indicates you can now execute a `Query`. The following is what you will see after starting:
```bash
$ python3 ./main.py ./conversation-files/{conversation}.csv
Starting...
Type 'help' to get a list of possible queries to execute
Type 'quit' to quit the program 
>>> 
```

## Query-Definitions and Query-Instances
`Query-Definition` refers to the TYPES of queries that can be asked. It provides a general pattern that can be used to generate a `Query-Instance`.

The most general form a `Query-Definition` can take is:
`{QueryDefinitionKeyword} {parameter(s)}`

For example, the `numMessagesSent` `Query-Definition`  looks like this:
`numMessagesSent BY {userX} FROM {dateX} @ {timeX} TO {dateY} @ {timeY}`
Where `numMessagesSent` is the `QueryDefinitionKeyword` and 
`BY {userX} FROM {dateX} @ {timeX} TO {dateY} @ {timeY}` are it’s `parameter(s)`

Likewise, every `Query-Instance` begins with a `QueryDefinitonKeyword`. 

Here are two `Query-Instances` for the `numMessagesSent` `Query-Definiton`:
`numMessagesSent BY user1 FROM 05.01.2018 @ 00:00 TO 05.02.2018 @ 00:00`
`numMessagesSent BY user2 FROM 06.30.2018 @ 13:00 TO 07.04.2018 @ 13:00`

The logic for each `Query-Definition` should live in its own `.py` file within the `./query_definitions/` directory

### Supported Query-Definitions
* `numMessagesSent`

### Not Yet Supported Query-Definitions
* `numOccurencesForWord`
* `averageResponseTime`
* `wordFrequency`

## Example Usage
```bash
$ python3 ./main.py ./conversation-files/sample-conversation.csv
Starting...
Type 'help' to get a list of possible queries to execute
Type 'quit' to quit the program 
>>> numMessagesSent BY user1 FROM 05.30.2018 @ 07:00 TO 06.01.2018 @ 08:00
2
>>> quit
Quitting...
$
```