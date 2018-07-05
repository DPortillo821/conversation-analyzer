# conversation-analyzer
## Overview
The purpose of this program is to do analysis on any given conversation between two users.
(NOTE: we hope to add multiple user functionality in the future) 
The program extracts information from the conversation that can then be queried once run. 
Refer to sections `How To Use` and `Query-Definitions and Query-Instances` for more details as to what type of queries can be asked and how they need to be asked as well as examples for each.

### Input
The input for this program is a text file that represents a conversation. 
The conversation should have the general structure that, for a given message there is, at minimum, a date, time, and user associated with it. 

(NOTE: The following conversation pattern is the only one that is currently supported)
For example, the text file can contain something that looks like this:
```
Thursday, 31 May 2018
30 May 2018 at 7:00 AM, user1 : hey!
31 May 2018 at 7:14 AM, user2 : what's up?
01 June 2018 at 7:47 AM, user1 : how are you?
```

(NOTE: we hope to add support for different types of conversation patterns in the future)
Where it could also look something like this:
```
Thursday, 05/31/2018
05/31/2018 @ 07:00, user1 : hey!
05/31/2018 @ 07:14, user2 : what's up?
05/31/2018 @ 07:47, user1 : how are you?
```

Whichever way the conversation is represented, at minimum, there should be a date, time, and user associated with each message.

### Output
The output of a `Query` depends on which `Query` was run. 
For example, you could run a `Query` that asks “How many messages did user1 send on May 31st 2018?”  and the expected output should be a positive integer.

A different `Query` can ask “How long, on average, did it take user1 to reply for messages sent on dateX in minutes?” and the expected output should be a positive number in minutes.

## How to run
You can start the program by running the following command within the command line:
```bash
python3 ./conversation-analyzer.py ./conversation-files/{conversation}.txt
```
Where `{conversation}` refers to the name of the text file which contains the conversation. Be sure the format of the conversation follows the same patterns described in the `Input` section.

## How to use
Once the program has started you will be prompted for a `Query`. The following is what you will see after starting:
```bash
$ python3 ./conversation-analyzer.py ./conversation-files/{conversation}.txt
Starting...
Type 'HELP' to get a list of possible queries to execute
Type 'QUIT' to quit the program 
>>> 
```

## Query-Definitions and Query-Instances
`Query-Definition` refers to the TYPES of queries that can be asked. It provides a general pattern that can be used to generate a `Query-Instance`.

The most general form a `Query-Definition` can take is:
`{QueryDefinitionKeyword} {parameter(s)}`

For example, the `numMessagesSent` `Query-Definition`  looks like this:
`numMessagesSent FROM {dateX} AT {timeX} TO {dateY} AT {timeY} FOR {userX}`
Where `numMessagesSent` is the `QueryDefinitionKeyword` and 
`FROM {dateX} AT {timeX} TO {dateY} AT {timeY} FOR {userX}` are it’s `parameter(s)`

Likewise, every `Query-Instance` begins with a `QueryDefinitonKeyword`. 

Here are two `Query-Instances` for the `numMessagesSent` `Query-Definiton`:
`numMessagesSent FROM 05/01/2018 AT 00:00 TO 05/02/2018 AT 00:00 FOR user1`
`numMessagesSent FROM 06/30/2018 AT 13:00 TO 07/04/2018 AT 13:00 FOR user2`

The logic for each `Query-Definition` should live in its own `.py` file within the `./models/` directory

### Supported Query-Definitions
* :( 

### Not Yet Supported Query-Definitions
* `numMessagesSent`
* `numOccurencesForWord`
* `averageResponseTime`
* `wordFrequency`

## Example Usage
```bash
$ python3 ./conversation-analyzer ./conversation-files/sample-conversation.txt
Starting...
Type 'HELP' to get a list of possible queries to execute
Type 'QUIT' to quit the program 
>>> HELP 
[
	'numMessagesSent',
	'numOccurencesForWord'
]
>>> HELP numMessagesSent
Query-Definition:
numMessagesSent FROM {dateX} [AT {timeX}] TO {dateY} [AT {timeY}] FOR {userX} [BY {unitOfTime}]
{dateX} and {dateY} should take the form MM/DD/YYYY
[AT {timeX}] and [AT {timeY}] are optional. Should take the form HH:MM (24-Hour Clock). Defaults to 00:00
[BY {unitOfTime}] is optional. If provided, must be either 'HOUR', 'DAY', 'MONTH', or 'YEAR'
Ex: numMessagesSent FROM 05/30/2018 AT 00:00 TO 06/02/2018 AT 00:00 FOR user1
>>> numMessagesSent FROM 05/30/2018 AT 00:00 TO 06/02/2018 AT 00:00 FOR user1
2
>>> numMessagesSent FROM 05/30/2018 AT 00:00 TO 06/02/2018 AT 00:00 FOR user1 BY DAY
{
	'05/30/2018': 5,
	'05/31/2018': 2,
	'06/01/2018': 7
}
>>> numMessagesSent FROM 05/30/2018 TO 06/02/2018 FOR user1 BY DAY
{
	'05/30/2018': 5,
	'05/31/2018': 2,
	'06/01/2018': 7
}
>>> numMessagesSent FROM 05/30/2018 TO 06/02/2018 FOR user1 BY MONTH
{
	'05/2018': 7,
	'06/2018': 7
}
>>> numMessagesSent FROM 05/30/2018 TO 06/02/2018 FOR user1 BY YEAR
{
	'2018': 14
}
>>> QUIT
Quiting...
$
```