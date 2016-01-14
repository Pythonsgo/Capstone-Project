# -*- coding: utf-8 -*-

# Author: Selma Gomez Orr <selmagomezorr@gmail.com> Copyright (C) October 12, 2015


##########################################################################
## Imports
##########################################################################

from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split as tts
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics

import numpy as np
import pickle


##########################################################################
## Module Constants
##########################################################################
##########################################################################
## Modules
##########################################################################
##########################################################################
## Program
##########################################################################

if __name__ == "__main__":

    corpus = load_files("Language_Folder")
 
    #print len(corpus.data)
 
    X_train, X_test, y_train, y_test = tts(corpus.data, corpus.target, test_size=0.20)
    
    
    text_clf = Pipeline([
        ('vec', CountVectorizer(analyzer='char_wb')),
        ('clf', MultinomialNB())
    ])
        
    text_clf = text_clf.fit(X_train, y_train)
    
    #Store the instance using pickle.
    with open('experiment_file','w') as f:
        pickle.dump(text_clf,f)
    
    
    predicted = text_clf.predict(X_test)
    accuracy = np.mean(predicted==y_test)
    print accuracy
    
    print "Here it is."

    random_test = ['самая большая страна в мире','campanili e cupole contro il verde intenso delle', 
                    'vérifiez auparavant que le sujet', 'this is a test', 'solo una prueba', 
                    'porzione più bassa della tastiera la seconda per quella più alta', 'nein', 'hello world',
                    'ข้าพเจ้าทำหนังสือเดินทางหาย ข้าพเจ้าควรทำอย่างไร', 'οὖν καὶ τὴν ἄλλην πόλιν καὶ περισκοπῶν τὰ ἀναθήματα, ὁρῶ',
                    'पूरा कर दिया था उसी पर उसने स्वयं ही नशतर रख दिया', 'ハロウィーンナゼ日本でブレイク', 'ওঠা এক শোকের মিছিল। মিছিলের',
                    'arrancou para um início de época prometedor', 'te zorgen dat de advertenties worden aangepast aan']
    
    
    predicted_random = text_clf.predict(random_test)
    print predicted_random
      
     
    
    