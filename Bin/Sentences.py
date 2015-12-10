import xlrd

LOGNAME="sentences.log"

class Sentences:
    sentenceToParse = []
    def __init__(self, sentencesFilename):
        sentencesLog = open(LOGNAME, 'w')
        sentencesFile = xlrd.open_workbook(filename=sentencesFilename, \
            verbosity=10, logfile = sentencesLog)
        sentencesLog.close()