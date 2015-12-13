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
                categoriesCSVFile = csv.reader(categoriesReadFile, delimiter=DELIMITATION)
                
                #Get category names
                categoriesList = categoriesCSVFile.next()
                categoriesMap = {}

                for row in categoriesCSVFile:
                    for x in range(len(row)):
                        if(row[x] != ''):
                            categoriesMap[row[x]] = x

            categoriesLog.close()
        except csv.Error as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except Exception:
            print "Categories Exception at __init__"
    
    # Returns the list of the category names
    def getNamesOfCategories(self):
        return categoriesList
    
    # Returns the name of the category for which the word belongs, or None
    def getWordsCategory(self, word):
        if(word in categoriesMap):
            return categoriesMap[word]
        else:
            return None