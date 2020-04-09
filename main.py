from textblob import TextBlob

def isSubjective(value):
    # 0.0 is very objective
    # 1.0 is very subjective
    if value > 0.5:
    	return True
    else: 
    	return False

def isPolarity(value):
    if value == 0:
	return 'Neutro'
    if value > 0:
    	return 'Positivo'
    else:
    	return 'Negativo'	

def main():
    text = '''
    Eu te amo. Joao pode ser um homem chato. Ratos gostam de Ratos. Hoje a sexta-feira vai ser linda.
    '''

    blob = TextBlob(text)
    blob.tags     
    blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])
    blob = blob.translate(to="en") 
    #print(blob)
    for sentence in blob.sentences:
    	print(sentence.words)
        print(sentence.sentiment)
        print("Polarity: " + str(isPolarity(sentence.sentiment.polarity)))
        print("Is Objective sentence?: " + str(isSubjective(sentence.sentiment.subjectivity)))  
        print("\n")
     # 'La amenaza titular de The Blob...'


if __name__ == "__main__":
	main()
