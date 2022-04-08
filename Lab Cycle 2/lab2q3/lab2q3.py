# -*- coding: utf-8 -*-
"""Lab2q3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RFqX17slmDx9vvakurkp4cJhJAwt35Yh

Q3. Read the file 'iris.json' as a text file.
1. Create a list having each line of the file as an element 
2. Convert it into a list of dictionary objects. 
3. Show the details of all flowers whose species is "setosa". 
4. Print the minimum petal area and max sepal area in each species 
5. Sort the list of dictionaries according to the total area are sepal and petal.
"""

import json

Json =  open('/content/iris.json', 'r')
jsonData = Json.read()
jsonList = json.loads(jsonData)

#1.list having each line of json as elements
print("List having each line of json as elements : ")
print(jsonList)
print("\n")

#2.list having dictionary of objects.
print("List of Dictionary Objects : ")
for i in jsonList:
  print(i)
print("\n")

#3.printing the details of only setosa.
print("Details of Flowers whose species is Setosa : ")
for i in jsonList:
  if(i['species']=='setosa'):
    print(i)

#list to store species names.
list_speciesName = list()
for i in jsonList:
  list_speciesName.append(i['species'])  

#converting the list to set inorder to remove duplicates.
list_speciesName = set(list_speciesName)

print('\n')
#initialising two list to store sepal and petal area.
sepal_area = list()
petal_area = list()
for i in list_speciesName:
  #printing the name of the species.
  print(i.capitalize())
  for j in jsonList:
    #calculates the petal and sepal area of each species.
    if(j['species']==i):
      sepal_area.append(j['sepalLength']*j['sepalWidth'])
      petal_area.append(j['petalLength']*j['petalWidth'])
  #prints the maximum sepal area and minimum petal area of each species.
  print("Maximum Sepal Area in ",i.capitalize()," is ",round(max(sepal_area),2))
  print("Minimum Petal Area in ",i.capitalize()," is ",round(min(petal_area),2))  
  print('\n')
  #list is cleared in order to save the area of one particular species at a time. 
  sepal_area.clear()
  petal_area.clear()
print('\n')

#copying the jsonList to another list.
jsonListCopy = list()
jsonListCopy = jsonList
for i in jsonListCopy:
  #calculating the petal area and sepal area.
  petal_area = (i["petalLength"]*i["petalWidth"])
  sepal_area = (i["sepalLength"]*i["sepalWidth"])
  total_area = (petal_area+sepal_area)
  i.update({'totalArea':total_area})

#sorting the list according of petal area and sepal area.
sortedList = (sorted(jsonListCopy, key = lambda i:i['totalArea'] ))
print("The Sorted List")

for i in sortedList:
  # i.pop('sepalArea')
  # i.pop('petalArea')
  # i.pop('totalArea)
  print(i)

Json.close()