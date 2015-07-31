#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################################
# This code is available under the MIT License.
# Ali Hashmi, MIT Center for Civic Media
# USING SVM, Multiple Binary Classifiers
###################################################################################
import pickle
import pprint, pickle
import numpy
import re
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import cross_validation
import time
import json
import datetime
from pandas.core.config_init import doc

class multiclassifier:

    def __init__(self):
        #subject list
        self.subjects = ['Accident and Disasters','Agriculture','Arts','Automotive',  \
            'Economy and Business' ,'Education','Energy','Environment','Fashion',  \
            "Feminism/Women's Issues/Gender Issues",'Food','Health','Politics',  \
            'Religion','Science and Technology','Sexuality','Sports','Travel', \
            'Weather']
        
        
        #class path
        xpath = "./multi/"
        
        #clfs and vectorizers
        self.clfs = [{"name":'Accident and Disasters', "serializedfile":xpath+"Acciden_LinearSVM.pkl", "vec":xpath+"Acciden_vec.pkl"},\
                {"name":'Agriculture', "serializedfile":xpath+"Agricul_LinearSVM.pkl", "vec":xpath+"Agricul_vec.pkl"},\
                {"name":'Arts', "serializedfile":xpath+"Arts_LinearSVM.pkl", "vec":xpath+"Arts_vec.pkl"},\
                {"name":'Auto', "serializedfile":xpath+"Automot_LinearSVM.pkl", "vec":xpath+"Automot_vec.pkl"},\
                {"name":'Economy and Business', "serializedfile":xpath+"Economy_LinearSVM.pkl", "vec":xpath+"Economy_vec.pkl"},\
                {"name":'Education', "serializedfile":xpath+"Educati_LinearSVM.pkl", "vec":xpath+"Educati_vec.pkl"},\
                {"name":'Energy', "serializedfile":xpath+"Energy_LinearSVM.pkl", "vec":xpath+"Energy_vec.pkl"},\
                {"name":'Environment', "serializedfile":xpath+"Environ_LinearSVM.pkl", "vec":xpath+"Environ_vec.pkl"},\
                {"name":'Fashion', "serializedfile":xpath+"Fashion_LinearSVM.pkl", "vec":xpath+"Fashion_vec.pkl"},\
                {"name":'Feminism/Women Issues/Gender Issues', "serializedfile":xpath+"Feminis_LinearSVM.pkl", "vec":xpath+"Feminis_vec.pkl"},\
                {"name":'Food', "serializedfile":xpath+"Food_LinearSVM.pkl", "vec":xpath+"Food_vec.pkl"},\
                {"name":'Health', "serializedfile":xpath+"Health_LinearSVM.pkl", "vec":xpath+"Health_vec.pkl"},\
                {"name":'Politics', "serializedfile":xpath+"Politic_LinearSVM.pkl", "vec":xpath+"Politic_vec.pkl"},\
                {"name":'Religion', "serializedfile":xpath+"Religio_LinearSVM.pkl", "vec":xpath+"Religio_vec.pkl"},\
                {"name":'Science and Technology', "serializedfile":xpath+"Science_LinearSVM.pkl", "vec":xpath+"Science_vec.pkl"},\
                {"name":'Sexuality', "serializedfile":xpath+"Sexuali_LinearSVM.pkl", "vec":xpath+"Sexuali_vec.pkl"},\
                {"name":'Sports', "serializedfile":xpath+"Sports_LinearSVM.pkl", "vec":xpath+"Sports_vec.pkl"},\
                {"name":'Travel', "serializedfile":xpath+"Travel_LinearSVM.pkl", "vec":xpath+"Travel_vec.pkl"},\
                {"name":'Weather', "serializedfile":xpath+"Weather_LinearSVM.pkl", "vec":xpath+"Weather_vec.pkl"}
                ]

    #encoding text
    def encode(self,string):
        clean_sentence_unwantedchars = '["\t\n ]+'
        string = string.encode('utf8')
        string = string.decode('utf-8')
        string = re.sub(clean_sentence_unwantedchars, ' ', string)
        string = string.encode('ascii', 'replace').encode('utf-8')
        string = string.decode('utf-8')
        return str(string)
 
    #this is the main function
    def classifyDocs2(self, FILENAME, OUTPUTFILENAME):
        
        #time stamping for reporting
        start_time = time.time()
        start_stamp = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
        corpusdata_docs = []
        
        #open the files, load it into array
        with open(FILENAME) as f:
            for line in f:
                strline = line.decode('utf-8')
                corpusdata_docs.append(self.encode(strline))
        print "documents cleaned:" + str(len(corpusdata_docs)) + " from file " + FILENAME
    
        #create JSON object
        for i in xrange(len(corpusdata_docs)):
            itemdict = {"topics":{},"docs":corpusdata_docs[i] }
            if i == 0:
                    strjson = '{"data": [' + json.dumps(itemdict)  
            if i < len(corpusdata_docs):
                    strjson = strjson + "," +json.dumps(itemdict)  
        strjson = strjson+ "]}"
        with open(OUTPUTFILENAME, 'w') as rjson:
            rjson.write(strjson)
        loadjson = open(OUTPUTFILENAME)
        
        #json object
        datajson = json.load(loadjson)
        
        #go through each binary classifier
        for items in self.clfs:
                #get clf
                clf_file = open(items["serializedfile"],'rb')
                classifier = pickle.load(clf_file)
                clf_file.close()
                
                #get vectorizer
                vec_file = open(items["vec"],'rb')
                vec = pickle.load(vec_file)
                vec_file.close()
                for doc in datajson["data"]:
                    #transform doc
                    datavec= vec.transform([doc["docs"]])
                    #add the class probability
                    doc["topics"][items["name"]]= str(round(classifier.predict_proba(datavec)[0][0]*100,2))
        #save file            
        with open(OUTPUTFILENAME, 'w') as outfile:
            json.dump(datajson,outfile, indent=4)
                
        #time stamping for reporting
        end_time = time.time()
        end_stamp = datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
        print start_stamp
        print end_stamp
        print end_time - start_time

def classifyDocs(FILENAME,OUTPUTJSONFILE):
    print "accessing classifiers..."
    objClass = multiclassifier()
    objClass.classifyDocs2(FILENAME,OUTPUTJSONFILE)
    print "results in file: /multi/" + OUTPUTJSONFILE  
    
    