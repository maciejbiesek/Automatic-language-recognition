import wikipedia
import wiki2plain
import sys
import string
import nltk    

wiki2plain = wiki2plain.Wiki2Plain()

def getArticles(lang, count):
    articles = []
    wikipedia.set_lang(lang)
    while len(articles) != count:
        try:
            randomArticle = wikipedia.random()
            print str(len(articles) + 1) + " " + randomArticle
            article = wikipedia.page(randomArticle)
            plainArticle = wiki2plain.plain(article.content)
            articles.append(article)
            with open("articles/" + lang + "/" + str(len(articles)), "w") as articleFile:
                articleFile.write(plainArticle.encode("ascii", "ignore"))
                
        except Exception as e:
            # do nothing
            print e
            # tu bedzie logger
    else:
        print lang + ' DONE'
        

getArticles("pl", 1000)
getArticles("en", 1000)
getArticles("de", 1000)
getArticles("fr", 1000)
getArticles("es", 1000)
