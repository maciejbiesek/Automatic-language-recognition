import article as art
import neural_network as net
import knn as k
import os
import random
import wikipedia
import wiki2plain
from sklearn import datasets

wiki2plain = wiki2plain.Wiki2Plain()
trainSet = []
testSet = []

def getFromDir(lang):
    lst =[]
    path = "articles/" + lang
    articlesFiles = os.listdir(path)

    for articleFile in articlesFiles:
        f = open(path + "/" + articleFile, "r")
        text = ""
        for line in f:
            text += line
        
        article = art.Article(articleFile, lang, text)
        article.normalize()

        lst.append(article)
    
    return lst


def sortToTrainAndTest(articles):
    for lang in articles:
        randomList = random.sample(range(1000), 200)
        
        for y in range(1000):
            if y in randomList:
                testSet.append(lang[y])
            else:
                trainSet.append(lang[y])
                
                
#def getArticle(lang):
    #articles = []
    #wikipedia.set_lang(lang)
    #while len(articles) != 1:
        #try:
            #randomArticle = wikipedia.random()
            #print randomArticle
            #article = wikipedia.page(randomArticle)
            #plainArticle = wiki2plain.plain(article.content)
            #print "\n\n" + plainArticle
            #articles.append(plainArticle)
            
                
        #except Exception as e:
            ## do nothing
            #print e
            ## tu bedzie logger
            
    #return articles[0]
    
        
polishArticles = getFromDir("pl")
englishArticles = getFromDir("en")
deutschArticles = getFromDir("de")
frenchArticles = getFromDir("fr")
spanishArticles = getFromDir("es")

articles = [ polishArticles, englishArticles, deutschArticles, frenchArticles, spanishArticles ]

sortToTrainAndTest(articles)

print "train set: " + str(len(trainSet))
print "test set: " + str(len(testSet))

network = net.NeuralNetwork(trainSet, testSet)
network.initializeNetwork()
network.testNetwork()

knn = k.knn(trainSet, testSet)
knn.initializeAlgorithm()
knn.testkNN()




    
