import csv

LOGNAME="categories.log"
DELIMITATION=','

class Categories:
    categoriesList = []
    categoriesMap = {}
    def __init__(self, categoriesFilename):
        try:
            categoriesLog = open(LOGNAME, 'w+')
        except IOError:
            categoriesLog = sys.stdout
        try:
            with open(categoriesFilename, 'rb') as categoriesReadFile:
                categoriesCSVFile = csv.reader(categoriesReadFile, delimiter=DELIMITATION)
                
                #Get category names
                self.categoriesList = categoriesCSVFile.next()

                for row in categoriesCSVFile:
                    for x in range(len(row)):
                        if(row[x] != ''):
                            self.categoriesMap[row[x]] = x

            categoriesLog.close()
        except csv.Error as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except Exception as e:
            print e
            print "Categories Exception at __init__"
    
    # Returns the list of the category names
    def getNamesOfCategories(self):
        return self.categoriesList
    
    # Returns the name of the category for which the word belongs, or None
    def getWordsCategory(self, word):
        wordStartsWith = ''
        for categoryKey in self.categoriesMap.keys():
            if(categoryKey.startswith(word)):
                wordStartsWith = categoryKey
                break;

        if(wordStartsWith in self.categoriesMap):
            return self.categoriesMap[word]
        else:
            return None