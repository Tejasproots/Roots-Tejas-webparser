from re import sub
from bs4 import BeautifulSoup
#importing the libraries
import numpy as np
# Pandas for managing datasets
import pandas as pd
#import requests (or urllib) to connect to the url
from googlesearch import search
import time
import re
import random
import requests
applications = ["site:bubbleapps.io","site:myshopify.com","site:wix.com","site:squarespace.com","site:mybigcommerce.com"]

country = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh",
           "Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi",
           "Côte d'Ivoire","Cabo Verde","Cambodia","Cameroon","Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo","Costa Rica","Croatia",
            "Cuba","Cyprus","Czechia","Democratic Republic of the Congo","Denmark","Djibouti","Dominica",
               "Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea",
               "Estonia","Eswatini","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana",
               "Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Holy See","Honduras","Hungary",
               "Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan",
               "Kazakhstan","Kenya","Kiribati","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Madagascar","Malawi",
               "Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco",
               "Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","New Zealand",
               "Nicaragua","Niger","Nigeria","North Korea","North Macedonia","Norway","Oman","Pakistan","Palau","Palestine State","Panama",
               "Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis",
               "Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe",
               "Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa",
               "South Korea","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Sweden","Switzerland","Syria",
               "Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey",
               "Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States of America",
               "Uruguay","Uzbekistan","Vanuatu","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]


variable = ["table","bike","sandals","slippers","clothing","furniture","books","dvd","paper","Blender","bin",
            "towels","toys","football","athletic","organic"]

#generating list of query -  Input for google.search package

# general application site
query1 = []
for a in applications :
    query1.append(a)
len(query1)

# country appended to application site
#Formatting country name 
countryname =[]
query2 =[]
for c in country:
    searchvariable= re.sub(r"\s", "", ""+c+"\t")
    countryname.append(searchvariable)
query2=[str(y)+":"+ x  for x in applications for y in countryname]
len(query2)

#random variable appended to application
query3 =[]
query3=[str(y)+":"+ x  for x in applications for y in variable]
len(query3)

#country + random variable 
queryrand = []
queryrand= [ x +" "+ str(y)  for x in countryname for y in variable]
len(queryrand)

#country + randon variable + application site
query4 = []
query4= [str(y)+":"+ x  for x in applications for y in queryrand]

finalquery= []
finalquery = query1+query3 ##+ query2 + query4
len(finalquery)


#links = []
#for q in finalquery:
#    query= q 
#    for j in search(query, num=1000, start=3, stop=1000, pause=(random.randint(5,20))):
#        result = re.search('https(.*).com/',j) #Regex to look for for specific patterns "https.......com"
#        
#        time.sleep(random.randit(5,40))
#        if result:
#            id = result.group()              
#            if id not in links:
#                links.append(id) #if regex passed and value not already in list append to list

links = []
for q in finalquery:
    query= q 
    for j in search(query, num_results=3):
        result = re.search('https(.*).com/',j) #Regex to look for for specific patterns "https.......com"
        
        time.sleep(random.randit(5,40))
        if result:
            id = result.group()              
            if id not in links:
                links.append(id) #if regex passed and value not already in list append to list

