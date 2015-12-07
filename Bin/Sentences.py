import xlrd

LOGNAME="sentences.log"

class Sentences:
    sentenceToParse = []
    def __init__(self, sentencesFilename):
        sentencesFile = xlrd.open_workbook(filename=sentencesFilename, \
            verbosity=10)