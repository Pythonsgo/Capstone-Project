# -*- coding: utf-8 -*-

# Author: Selma Gomez Orr <selmagomezorr@gmail.com> Copyright (C) October 12, 2015


##########################################################################
## Imports
##########################################################################

import pickle
import numpy as np


##########################################################################
## Constants
##########################################################################
Language_list = ['Bengali', 'Dutch', 'English', 'French', 'German', 'Greek',
                 'Hindi', 'Italian', 'Japanese', 'Portuguese', 'Russian', 'Spanish', 'Thai']

##########################################################################
## Modules

##########################################################################


##########################################################################
## Program
##########################################################################

if __name__ == "__main__":
    
    #Load the model using pickle.
  
    text_clf = pickle.load(open('experiment_file','r'))
    
    
    #Select random text from different languages to test."
    
    test_string = raw_input("Enter your sample text:")
    
    test_string = [test_string]
    
    predict_string = text_clf.predict(test_string)
    
    print "This test text is written in:", Language_list[predict_string]
    

    

    random_test = ['самая большая страна в мире','campanili e cupole contro il verde intenso delle', 
                    'vérifiez auparavant que le sujet', 'this is a test', 'solo una prueba', 
                    'porzione più bassa della tastiera la seconda per quella più alta', 
                    'Das Polaritätsprofil für das', 'hello world',
                    'ข้าพเจ้าทำหนังสือเดินทางหาย ข้าพเจ้าควรทำอย่างไร', 'οὖν καὶ τὴν ἄλλην πόλιν καὶ περισκοπῶν τὰ ἀναθήματα, ὁρῶ',
                    'पूरा कर दिया था उसी पर उसने स्वयं ही नशतर रख दिया', 'ハロウィーンナゼ日本でブレイク', 'ওঠা এক শোকের মিছিল। মিছিলের',
                    'arrancou para um início de época prometedor', 'te zorgen dat de advertenties worden aangepast aan',
                    'Solo una prueba para ver el resultado', 'Just another test.']
    
    
 
 
    
    
    
      
     
