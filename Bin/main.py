import Categories
import Sentences
import logging
import csv
import copy

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
    logging.debug("Completed creating categories object")
    sentences = Sentences.Sentences(SENTENCESFILE)
    logging.debug("Completed extracting sentences")
    output = createOutputFile()
    logging.debug("Completed creating outputfile")
    output.writerow(categories.getNamesOfCategories())
    logging.debug("Completed writing category names")
    matchWordsToSentence(categories, sentences, output)
    
def createOutputFile():
    try:
        csvOut = open(OUTPUTFILE, 'w')
        return csv.writer(csvOut, delimiter = ',')
    except:
        print "Exception creating output file. Will write result to screen"
        return sys.stdout
        
def matchWordsToSentence(categories, sentences, output):
    emptyRow = []
    for x in range(len(categories.getNamesOfCategories())):
        emptyRow.append(0)

    for sentence in sentences.getSentences():
        currentRow = copy.deepcopy(emptyRow)
        logging.debug("sentence: {0}".format(sentence))
        for word in sentence[0].split():
            wordCategoryInt = categories.getWordsCategory(word)
            if(wordCategoryInt is not None):
                currentRow[wordCategoryInt] = currentRow[wordCategoryInt] + 1
        output.writerow(currentRow)

if(__name__=='__main__'):
    main()