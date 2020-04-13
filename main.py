from twitter import Twitter
from db import Database
from datetime import datetime 
from emotion import EmotionTwitter


def main():
    text = '''
    Eu te amo. Joao pode ser um homem chato. Hoje a sexta-feira vai ser linda. Joao o mais bobo.
    '''
    tag = "Nintendo"

    em = EmotionTwitter(text,"pt","en")
    em.sentences()
    listtwitter = []
    twitter = Twitter( datetime.now().strftime("%m/%d/%Y"), tag, em.polarity, em.objective)
    listtwitter.append(twitter)

    db = Database("db_twitter_emotion") 
    db.removeAll()
    db.insertList(listtwitter)

    for i in db.findAll():
    	print(i)

if __name__ == "__main__":
  main()

