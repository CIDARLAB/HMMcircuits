
# coding: utf-8

# In[12]:

import ast #to convert the text file of lists to real lists
import re #import regex - regular expressions

def convertCircuitList(fileSource):
    listOfCircuits  = ast.literal_eval(open(fileSource).read())
    for sublist in listOfCircuits:
        for substring in sublist:
            if type(substring)==str:
                #series of if statements and regex to check which transcriptional unit (?) it is and make a dict with label
                if re.findall(r"[p]\S", substring):
                    listOfCircuits[listOfCircuits.index(sublist)][sublist.index(substring)] = {substring:"promoter"}
                elif re.findall(r"[Ribo]\S", substring):
                    listOfCircuits[listOfCircuits.index(sublist)][sublist.index(substring)] = {substring:"ribosome"}
                elif re.findall(r"\b[A-Z][\d]{1}", substring):
                    listOfCircuits[listOfCircuits.index(sublist)][sublist.index(substring)] = {substring:"ribosyme binding site"}
                elif re.findall(r"\b[A-Z][a-zA-Z]+$", substring):
                    listOfCircuits[listOfCircuits.index(sublist)][sublist.index(substring)] = {substring:"coding sequence"}
                elif re.findall(r"[ECK][\d]+$", substring):
                    listOfCircuits[listOfCircuits.index(sublist)][sublist.index(substring)] = {substring:"terminator"}
    return listOfCircuits

g = convertCircuitList("/Users/Kaveri/Documents/RISE/Data_of_circuits/good_circuits.txt")
print g


# In[18]:

#inputtedSequence is the list that the user inputs which has the sequences of parts they want
#listOfCircuits is the list of dictionaries for every element in the circuits - good/bad
def breakingUpCircuits(inputtedSequence, listOfListsOfCircuits):  
    #this is the empty list to fill
    sequenceOfParts=[]
    for listOfCircuits in listOfListsOfCircuits:
        #these are the counters for the lists.
        inputtedSequenceCounter=0
        listOfCircuitsCounter=0
        subSequenceOfParts=[]
        #this is for making a list of lists of final sequence part

        #loop to iterate through the listOfCircuits
        while listOfCircuitsCounter<len(listOfCircuits):
            subSubSequenceOfParts=[]
            insideLoop= False

            #check that while conditions are fine
            while inputtedSequenceCounter<(len(inputtedSequence)) and listOfCircuitsCounter<len(listOfCircuits) and inputtedSequence[inputtedSequenceCounter]==listOfCircuits[listOfCircuitsCounter].values()[0]:
                subSubSequenceOfParts.append(listOfCircuits[listOfCircuitsCounter].keys()[0])
                insideLoop=True
                inputtedSequenceCounter=inputtedSequenceCounter+1
                listOfCircuitsCounter=listOfCircuitsCounter+1
                if inputtedSequenceCounter==len(inputtedSequence):
                    subSequenceOfParts.append(subSubSequenceOfParts)
                    #this is to cancel out the incrementing of that occured before and after. 
            #if it has already been in the while loop, it already has the last listOfCircuitsCounter=listOfCircuitsCounter+1 so it doesn't need another     
            if insideLoop==False:
                listOfCircuitsCounter=listOfCircuitsCounter+1
            #use the initial position of the InputtedSequenceCounter
            inputtedSequenceCounter=0
            
        sequenceOfParts.append(subSequenceOfParts)
    print sequenceOfParts
   


# In[19]:

goodCircuits = convertCircuitList("/Users/Kaveri/Documents/RISE/Data_of_circuits/good_circuits.txt")
breakingUpCircuits(['promoter','ribosome','ribosyme binding site','coding sequence','terminator'],goodCircuits)


# In[ ]:



