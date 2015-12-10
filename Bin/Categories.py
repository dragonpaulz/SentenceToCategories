import xlrd

LOGNAME="categories.log"

class Categories:
    mapWordsToCategories = []
    def __init__(self, categoriesFilename):
        categoriesLog = open(LOGNAME, 'w')
        categoriesFile = xlrd.open_workbook(filename=categoriesFilename, \
            verbosity=10, logfile = categoriesLog)
        categoriesLog.close()