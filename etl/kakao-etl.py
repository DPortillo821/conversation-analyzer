# transform file to only have one record per line
# seek lines that have the format Thursday, 30 May 2018 (this is an indicator that the next line is the beginning)
# read next line and grab datetime and user and partial content
# scan next line and see if there is a new line followed by a line that has the previously mentioned pattern
# if that's not the case then the next line is part of the content