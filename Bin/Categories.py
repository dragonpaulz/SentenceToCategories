import xlrd

LOGNAME="categories.log"

class Categories:
    mapWordsToCategories = []
    def __init__(self, categoriesFilename):
        categoriesFile = xlrd.open_workbook(filename=categoriesFilename, \
            verbosity=10)