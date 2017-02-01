#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(len(enron_data))
print("Number of values per person", len(enron_data["SKILLING JEFFREY K"].keys()))
'''
countPOI = 0

#for each string k in pickled dictionary enron_data.
for k in enron_data:
    #print(enron_data[k]['poi'])
    if (enron_data[k]['poi']):
        countPOI+= 1
'''
#print(enron_data.values())
#print(enron_data.viewkeys())


#1
#print("Number of people of interest : ", countPOI)

#2
#print(enron_data["PRENTICE JAMES"]['total_stock_value'])

#2
#print("Colwell to poi :  " + str(enron_data["COLWELL WESLEY"]['from_this_person_to_poi']))

#3
#print("Skilling exercised options :  " + str(enron_data["SKILLING JEFFREY K"]['exercised_stock_options']))

#follow the money
#print("Lay total payments :  " + str(enron_data["LAY KENNETH L"]['total_payments']))
#print("Skilling total payments :  " + str(enron_data["SKILLING JEFFREY K"]['total_payments']))
#print("Fastow total payments :  " + str(enron_data["FASTOW ANDREW S"]['total_payments']))

#dealing with unfilled features
countQS = 0

#for each string k in pickled dictionary enron_data.
for k in enron_data:
    if not(enron_data[k]['salary'] == "NaN"):
        countQS+= 1

print(countQS)

countEmail = 0

#for each string k in pickled dictionary enron_data.
for k in enron_data:
    if not(enron_data[k]['email_address'] == "NaN"):
        countEmail+= 1

print(countEmail)



