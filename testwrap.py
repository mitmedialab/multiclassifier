#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################################
# This code is available under the MIT License.
# Ali Hashmi, MIT Center for Civic Media
# USING SVM, Multiple Binary Classifiers
###################################################################################

import multi
#clfs = [{"name":'Accident and Disasters', "serializedfile":"Acciden_LinearSVM.pkl", "vec":"Acciden_vec.pkl"},\
#        {"name":'Agriculture', "serializedfile":"Agricul_LinearSVM.pkl", "vec":"Agricul_vec.pkl"},\
#        {"name":'Arts', "serializedfile":"Arts_LinearSVM.pkl", "vec":"Arts_vec.pkl"},\
#        {"name":'Auto', "serializedfile":"Automot_LinearSVM.pkl", "vec":"Automot_vec.pkl"},\
#        {"name":'Economy and Business', "serializedfile":"Economy_LinearSVM.pkl", "vec":"Economy_vec.pkl"},\
#        {"name":'Education', "serializedfile":"Educati_LinearSVM.pkl", "vec":"Educati_vec.pkl"},\
#        {"name":'Energy', "serializedfile":"Energy_LinearSVM.pkl", "vec":"Energy_vec.pkl"},\
#        {"name":'Environment', "serializedfile":"Environ_LinearSVM.pkl", "vec":"Environ_vec.pkl"},\
#        {"name":'Fashion', "serializedfile":"Fashion_LinearSVM.pkl", "vec":"Fashion_vec.pkl"},\
#        {"name":'Feminism/Women Issues/Gender Issues', "serializedfile":"Feminis_LinearSVM.pkl", "vec":"Feminis_vec.pkl"},\
#        {"name":'Food', "serializedfile":"Food_LinearSVM.pkl", "vec":"Food_vec.pkl"},\
#        {"name":'Health', "serializedfile":"Health_LinearSVM.pkl", "vec":"Health_vec.pkl"},\
#        {"name":'Politics', "serializedfile":"Politic_LinearSVM.pkl", "vec":"Politic_vec.pkl"},\
#        {"name":'Religion', "serializedfile":"Religio_LinearSVM.pkl", "vec":"Religio_vec.pkl"},\
#        {"name":'Science and Technology', "serializedfile":"Science_LinearSVM.pkl", "vec":"Science_vec.pkl"},\
#        {"name":'Sexuality', "serializedfile":"Sexuali_LinearSVM.pkl", "vec":"Sexuali_vec.pkl"},\
#        {"name":'Sports', "serializedfile":"Sports_LinearSVM.pkl", "vec":"Sports_vec.pkl"},\
#        {"name":'Travel', "serializedfile":"Travel_LinearSVM.pkl", "vec":"Travel_vec.pkl"},\
#        {"name":'Weather', "serializedfile":"Weather_LinearSVM.pkl", "vec":"Weather_vec.pkl"}
#        ]


FILENAME = "./multi/inputfile.txt"
#inputfile, each doc on a separate line

OUTPUTJSONFILE = "./multi/outputfile.json"
# output file where classification data is saved

#usage
multi.classifyDocs(FILENAME,OUTPUTJSONFILE)
# Use the one with max value

#{
#    "data": [
#        {
#            "docs": "Balochistan University Staffers Protest Funds Scarcity QUETTA - Scores of teachers and staff of the University of Balochistan continued their protest against the govt for not providing adequate financial assistance, paralysing educational activities at the largest and oldest state-run varsity of the province.The teachers and other staff staged a unique type of protest by begging outside the Chief Minister House, and announced to set up a camp at Quetta Hockey Chowk from Dec 6. The decision to this effect was taken by the Balochistan University Joint Action Committee during a protest demonstration outside the varsity gate.Addressing on the occasion, Academic Staff Association members Dr Kaleemullah Bareech, Prof Abdul Baqi Jattak, Haji Abdul Aziz Langov, Alam Khan Kharoti and others said that the government has failed to substantiate its promises made during the May 11 General Elections. They said there is no money to be paid as far as salaries of the UoB teachers and other staffs are concerned.How the dream of higher education could be fulfilled under such circumstances,? they said and added that the sitting UoB vice chancellor did not have the capacity to run the varsity affairs.They demanded the government to sack the incumbent VC and run the varsity in accordance with the University Act 1996. ", 
#            "topics": {
#                "Feminism/Women Issues/Gender Issues": "20.13", 
#                "Arts": "1.43", 
#                "Fashion": "0.67", 
#                "Sports": "1.84", 
#                "Food": "10.78", 
#                "Auto": "2.49", 
#                "Energy": "1.91", 
#                "Science and Technology": "10.53", 
#                "Accident and Disasters": "0.59", 
#                "Sexuality": "1.65", 
#                "Environment": "1.85", 
#                "Religion": "15.69", 
#                "Economy and Business": "1.21", 
#                "Health": "5.19", 
#                "Weather": "6.42", 
#                "Politics": "68.46", 
#                "Education": "98.8", 
#                "Agriculture": "1.05", 
#                "Travel": "1.5"
#            }
#        }, 



