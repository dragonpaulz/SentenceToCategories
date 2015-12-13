import csv

LOGNAME="categories.log"
DELIMITATION=','

class Categories:
    mapWordsToCategories = []
    def __init__(self, categoriesFilename):
        try:
            categoriesLog = open(LOGNAME, 'w')
        except IOError:
            categoriesLog = sys.stdout
        try:
            with open(categoriesFilename, 'rb') as categoriesReadFile:
                csv.reader(categoriesReadFile, delimiter=DELIMITATION)

            categoriesLog.close()
        except csv.Error as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except error as e:
            print "Categories error ({0}): {1}".format(e.errno, e.strerror)