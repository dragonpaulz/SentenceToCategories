import csv

LOGNAME="sentences.log"
DELIMITATION=','

class Sentences:
    sentenceToParse = []
    def __init__(self, sentencesFilename):
        try:
            sentencesLog = open(LOGNAME, 'w')
        except IOError:
            categoriesLog = sys.stdout
        try:
            with open(sentencesFilename, 'rb') as sentencesReadFile:
                sentences = csv.reader(sentencesReadFile, delimiter=DELIMITATION)
                for sentence in sentences:
                    print sentence
                
            sentencesLog.close()
        except csv.Error as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except Exception:
            print "Sentences Exception at __init__"
            