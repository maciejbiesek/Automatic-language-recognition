import numpy as np
from pybrain.supervised import BackpropTrainer
from pybrain import TanhLayer, SoftmaxLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets.classification import ClassificationDataSet

class NeuralNetwork:
    
    def __init__(self, train, test):
        self.encodingDict = {
            "pl": 0,
            "en": 1,
            "de": 2,
            "fr": 3,
            "es": 4,
        }
        
        self.train = train
        self.test = test
        
    def initializeNetwork(self):        
        self.net = buildNetwork(26, 15, 5, hiddenclass=TanhLayer, outclass=SoftmaxLayer) # 15 is just a mean
        ds = ClassificationDataSet(26, nb_classes=5)
        
        for x in self.train:
            ds.addSample(x.frequency, self.encodingDict[x.lang])
        ds._convertToOneOfMany()

        trainer = BackpropTrainer(self.net, dataset=ds, weightdecay=0.01, momentum=0.1, verbose=True)
        trainer.trainUntilConvergence(maxEpochs=100)
        
    def testNetwork(self):
        correctAnswers = []
        for testItem in self.test:
            correctAnswers.append(self.encodingDict[testItem.lang])
        
        ds_test = ClassificationDataSet(26, nb_classes=5)
        for x in self.test:
            ds_test.addSample(x.frequency, self.encodingDict[x.lang])
        ds_test._convertToOneOfMany()

        sumCorrect = sum(self.net.activateOnDataset(ds_test).argmax(axis=1) == correctAnswers)
        
        print "\nNeural network: " + str(sumCorrect*100/float(len(self.test))) + "% efficiency"
        
        