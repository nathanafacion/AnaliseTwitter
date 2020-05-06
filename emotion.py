from textblob import TextBlob
import collections

import createlog 
logger = createlog.logger

class EmotionTwitter:
    def __init__(self, text, from_lang):
	
	try:
	    self.blob = TextBlob(text).translate(from_lang = from_lang, to='en')
	except:
	    self.blob = TextBlob(text)
       
        
        self.objective = None
        self.polarity = None 

    def isObjective(self,value):
        # 0.0 is very objective
        # 1.0 is very subjective
        if value > 0.5:
    	    return 'No'
        else: 
    	    return 'Yes'

    def definePolarity(self,value):
        if value == 0:
	    return 'Neutro'
        if value > 0:
    	    return 'Positive'
        else:
    	    return 'Negative'	


    def returnMoreCommon(self,list, value_default):
    	# Pegamos os maiores resultados, pois queremos saber a emocao mais presente no twitter todo
    	# se os dois primeiros elementos tiverem mesmo valor entao usamos um valor default como resposta
    	# senao vamos retornar a chave do maior valor
    	data = collections.Counter(list).most_common(2)
    	logger.info('List: ')
    	logger.info(list)
    	if len(data)!=1 and data[0][1] == data[1][1]:
    		return value_default
    	else:
            return data[0][0]

    def sentences(self):
    	polarities = []
    	isObjectives = []
    	for sentence in self.blob.sentences:
    	    polarities.append(str(self.definePolarity(sentence.sentiment.polarity)))
    	    isObjectives.append(str(self.isObjective(sentence.sentiment.subjectivity)))

        self.objective = self.returnMoreCommon(isObjectives, 'No')
        self.polarity = self.returnMoreCommon(polarities,'Neutro')
        logger.info('Objetive: '+self.objective)
        logger.info('Polarity: '+self.polarity)
