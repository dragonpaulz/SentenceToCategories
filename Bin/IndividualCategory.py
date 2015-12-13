class IndividualCategory:
    def __init__(self, categoryName, mapOfWords):
        category = categoryName, mapOfWords

    def wordInCategory(self, potentialMatch):
        return potentialMatch in self.mapOfWords