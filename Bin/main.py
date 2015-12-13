import Categories
import Sentences
import logging

#configuration:
CATEGORIESFILE="..\Data\Categories.csv"
SENTENCESFILE="..\Data\Sentences.csv"
LOGGERFILE="ParserLog.log"
LOGGERDETAIL=logging.INFO
FORMAT="Level:%(levelno)s\tModule:%(module)s\tLine:%(lineno)d\t%(message)s"

def main():
    logging.basicConfig(filename=LOGGERFILE, level=LOGGERDETAIL, format=FORMAT)
    logger = logging.getLogger(LOGGERFILE)
    logging.info("Process begins")
    categories = Categories.Categories(CATEGORIESFILE)
    sentences = Sentences.Sentences(SENTENCESFILE)

if(__name__=='__main__'):
    main()