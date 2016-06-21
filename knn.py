from sklearn.neighbors import KNeighborsClassifier

class knn:
    
    def __init__(self, train, test):
        self.train_freq = []
        self.train_lang = []
        
        self.test_freq = []
        self.test_lang = []
        
        for trainItem in train:
            self.train_freq.append(trainItem.frequency)
            self.train_lang.append(trainItem.lang)
            
        for testItem in test:
            self.test_freq.append(testItem.frequency)
            self.test_lang.append(testItem.lang)
            
    def initializeAlgorithm(self):
        self.knn = KNeighborsClassifier(metric='minkowski', n_neighbors=1, p=2)
        self.knn.fit(self.train_freq, self.train_lang)
        
    def testkNN(self):
        counter = 0
        
        predict = self.knn.predict(self.test_freq)
        
        for i in range(len(predict)):
            if predict[i] == self.test_lang[i]:
                counter += 1
                
        print "kNN: " + str(counter*100/float(len(self.test_lang))) + "% efficiency\n"
        
    def tryOne(self, oho):
        print "kNN prediction: " + self.knn.predict(oho)
        
        