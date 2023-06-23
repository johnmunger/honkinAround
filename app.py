import constants
from random import randint
def printSentence():
    posLengthDict = {'ARTICLE':len(constants.WORDS_BY_POS['ARTICLE'])-1,
    'NOUN':len(constants.WORDS_BY_POS['NOUN'])-1,
    'ADJECTIVE':len(constants.WORDS_BY_POS['ADJECTIVE'])-1,
    'ADVERB':len(constants.WORDS_BY_POS['ADVERB'])-1,
    'PREPOSITION':len(constants.WORDS_BY_POS['PREPOSITION'])-1,
    'VERB':len(constants.WORDS_BY_POS['VERB'])-1,
    'INTERJECTION':len(constants.WORDS_BY_POS['INTERJECTION'])-1,
    'CONJUNCTION':len(constants.WORDS_BY_POS['CONJUNCTION'])-1,
    'PRONOUN':len(constants.WORDS_BY_POS['PRONOUN'])-1,
    'NUMERAL':len(constants.WORDS_BY_POS['NUMERAL'])-1}

    sentenceStructure = getSentenceStructure()
    sentence = []
    for i in range(len(sentenceStructure)):
        pos = sentenceStructure[i].upper()
        randomPosNumber = randint(0,posLengthDict[pos])
        sentence.append(constants.WORDS_BY_POS[pos][randomPosNumber])
    return sentence

def getSentenceStructure():
    someIndex = randint(0,len(constants.SENTENCE_STRUCTURE)-1)
    return constants.SENTENCE_STRUCTURE[someIndex]

def main():
    for i in range(50):
        printSentence()
    
if __name__ == "__main__":
    main()