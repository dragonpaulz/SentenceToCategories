import Categories
import Sentences
import logging
import csv

#configuration:
CATEGORIESFILE="..\Data\Categories.csv"
SENTENCESFILE="..\Data\Sentences.csv"
LOGGERFILE="ParserLog.log"
LOGGERDETAIL=logging.INFO
FORMAT="Level:%(levelno)s\tModule:%(module)s\tLine:%(lineno)d\t%(message)s"
OUTPUTFILE="..\OutputFile.csv"

def main():
    logging.basicConfig(filename=LOGGERFILE, level=LOGGERDETAIL, format=FORMAT)
    logger = logging.getLogger(LOGGERFILE)
    logging.info("Process begins")
    categories = Categories.Categories(CATEGORIESFILE)
    logging.info("Completed creating categories object")
    sentences = Sentences.Sentences(SENTENCESFILE)
    logging.info("Completed extracting sentences")
    output = createOutputFile()
    output.writerow(categories.getNamesOfCategories())
    
def createOutputFile():
    try:
        with open(OUTPUTFILE, 'w') as csvOut:
            return csv.writer(csvOut, delimiter = ',')
    except:
        print "Exception creating output file. Will write result to screen"
        return sys.stdout

if(__name__=='__main__'):
    main()