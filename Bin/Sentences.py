import csv

LOGNAME="sentences.log"
DELIMITATION=','

class Sentences:
    sentenceToParse = []
    def __init__(self, sentencesFilename):
        try:
            sentencesLog = open(LOGNAME, 'w')
        except IOError as E:
            categoriesLog = sys.stdout
        try:
            with open(sentencesFilename, 'rb') as sentencesReadFile:
                csv.reader(sentencesFilename, delimiter=DELIMITATION)
            sentencesLog.close()
        except csv.Error as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except error as e:
            print "Error ({0}): {1}".format(e.errno, e.strerror)