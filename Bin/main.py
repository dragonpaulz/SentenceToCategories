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
    createOutputFile()
    
def createOutputFile():
    with open(OUTPUTFILE, 'w') as csvOut:
        output = csvOut.write(csvOut, delimeter = ',')

if(__name__=='__main__'):
    main()