
# coding: utf-8

# In[72]:

#class Node creates nodes with properties state, edge, incoming, outgoing, weights, probabilities
class Node:
    def __init__(self):
        self.state = None
        self.output = {}
        self.outgoing = []
        self.incoming = []
    def setState(self, state):
        self.state = state
    def addOutgoingEdge(self, edge):
        self.outgoing.insert(0,edge)
    def removeOutgoingEdge(self, edge):
        self.outgoing.remove(edge)
    def addIncomingEdge(self,edge):
        self.incoming.insert(0,edge)
    def removeIncomingEdge(self,edge):
        self.incoming.remove(edge)
    def setOutput(self,outputDict):
        self.output = outputDict
    def setOutputDefault(self,outputkey):
        self.output[outputkey] = 1
        
    #dictionary to deal with multiple outputs in a node
    def setOutputMultiple(self,outputPairs):
        keysList = self.output.keys()+outputPairs.keys()
        uniqueKeysList = list(set(keysList))
        countDict = {}
        probDict = {}
        print self.output
        for key in uniqueKeysList:
            countDict[key] = keysList.count(key)
        for key in uniqueKeysList:
            probDict[key] = float(round(float(countDict[key])/len(keysList),2))
        self.output = probDict
        return probDict,countDict   
        
#class edge creates edges with properties probability, node from and node to       
class Edge:
    def __init__(self):
        self.nodeFrom = None
        self.nodeTo = None
        self.prob = 1.0
        self.weight = 1
    
    #the probability of the edge is the probability that the outgoing edge will be taken while departing from the node
    def setProbability(self, prob):
        self.prob = prob
    def setNodeFrom(self, nodeFrom):
        self.nodeFrom = nodeFrom  
    def setNodeTo(self,nodeTo):
        self.nodeTo = nodeTo  
    
    #the weight of an edge is how many times the edge is traversed while creating the circuits
    def setWeight(self,additionalWeight):
        self.weight = self.weight+additionalWeight
        
#http://stackoverflow.com/questions/17014211/iterate-python-nested-lists-efficiently
def traverse(item):
    try:
        for i in iter(item):
            for j in traverse(i):
                yield j
    except TypeError:
        yield item

#this function creates the circuit from a string and does step 1 of merging:
#connecting all circuits to initial&final nodes, making states numbers continuous, adding probability from initial     
def createInitialModel(circuitList):
    nodesList = []
    edgesList = []
    initialNode = Node()
    initialNode.setState('i')
    nodesList.append(initialNode)
    counter = 1
    finalNode = Node()
    finalNode.setState('f')
    nodesList.append(finalNode)
    #outer for loop gets each string within circuitList, the main input. the first node is created
    for circuitString in circuitList:
        secondNode = initialNode
        #second node is created, edge added in between them, properties added for the 3 objects        
        
        for i in circuitString:
            firstNode = secondNode
            newEdge = Edge()
        
            secondNode = Node()
            secondNode.setState(counter)
            secondNode.setOutputDefault(i)
            secondNode.addIncomingEdge(newEdge)
            firstNode.addOutgoingEdge(newEdge)
            newEdge.setNodeFrom(firstNode)
            newEdge.setNodeTo(secondNode)
            nodesList.append(secondNode)
            edgesList.append(newEdge)
            counter = counter + 1
        
        edgeToFinal = Edge()
        edgeToFinal.setNodeTo(finalNode)
        edgeToFinal.setNodeFrom(secondNode)
        edgesList.append(edgeToFinal)
        finalNode.addIncomingEdge(edgeToFinal)
        secondNode.addOutgoingEdge(edgeToFinal)
        #adding nodesList and edges List to mergedNodesList and mergedEdgesList. Flattening nested lists and printing

        nodesList = [i for i in traverse(nodesList)]
        edgesList = [i for i in traverse(edgesList)]
        #add probabilities to edges if 2 or more edges are going out of a node.
        for k in nodesList:
            if len(k.outgoing)>1:
                for j in k.outgoing:
                    j.setProbability(1.0/len(k.outgoing))

    print 'Nodes first function', len(nodesList)        
    for j in nodesList:
        print 'Output:',j.output,' State:',j.state, 'Node'
        for k in j.incoming:
            print 'Incoming:','from:', k.nodeFrom.state,k.nodeFrom.output,'to:',k.nodeTo.state,k.nodeTo.output
        for l in j.outgoing:
            print 'Outgoing:', 'from:', l.nodeFrom.state,l.nodeFrom.output,'to',l.nodeTo.state,l.nodeTo.output    
        print 
    
    print 'Edges first function', len(edgesList)
    for k in edgesList:
        print 'Probability:',k.prob,'Weight:',k.weight, 'Node from:',k.nodeFrom.output,k.nodeFrom.state,'Node to:',k.nodeTo.output,k.nodeTo.state
    print 
    return nodesList,edgesList


# In[73]:

#conducts merge 1 - merges nodes 1 and 3. 
#Finally, when I finish the function to find the 2 that need to be merged I can have a statement like this: node1,node2 = findNodesToMerge(circuitList)
def merge2Nodes(state1,state2,nodesList,edgesList):
    print  '__________________________________'
    #create node1 and node2 from the inputed states, state1 and state2
    nodeStates1 = []
    for node in nodesList:
        if node.state!='i'and node.state!='f':
            nodeStates1.append(node.state)
    print 'MERGE 1 FUNCTION NODE STATES',nodeStates1
    
    for node in nodesList:
        if node.state == state1:
            node1 = node
        elif node.state == state2:
            node2 = node
    
    #swapping nodes 1 and 2 if node 1 has a greater state than node 2       
    if node1.state>node2.state:
        node1,node2 = node2,node1
    
    #making the output of the new node
    if len(node1.output)==1 and len(node2.output) ==1 and node1.output == node2.output:
        pass
    elif node1.output != node2.output:
        node1.setOutputMultiple(node2.output)
    
    #adding a new incoming edge to node1 IF node 1 and node 2 don't come from the same node
    print 'Node1:',node1.state,node1.output
    print 'Node2:',node2.state,node2.output
    print ''
    
    #removing the incoming and outgoing edges of node 2 from edgesList
    for p in range(0,len(node2.outgoing)):
        edgesList.remove(node2.outgoing[p])
    for q in range(0,len(node2.incoming)):
        edgesList.remove(node2.incoming[q])

    
    for i in node2.incoming:
        node2Incoming = Edge()
        node2Incoming.setNodeTo(node1)
        node2Incoming.setNodeFrom(i.nodeFrom)
        edgesList.append(node2Incoming)
        node1.addIncomingEdge(node2Incoming)
        #keep removing edges so incoming[0] is different every time 
        i.nodeFrom.addOutgoingEdge(node2Incoming)
        i.nodeFrom.removeOutgoingEdge(i)
        node2.removeIncomingEdge(i)

    #adding a new outgoing edge to node1 IF node 1 and node 2 don't go to the same node
    for j in node2.outgoing:
        node2Outgoing = Edge()
        node2Outgoing.setNodeFrom(node1)
        node2Outgoing.setNodeTo(j.nodeTo)
        edgesList.append(node2Outgoing)
        node1.addOutgoingEdge(node2Outgoing)
        j.nodeTo.addIncomingEdge(node2Outgoing)
        j.nodeTo.removeIncomingEdge(j)
        node2.removeOutgoingEdge(j)
                
    nodesList.remove(node2)
    for node in nodesList:
        node.incoming = [i for i in traverse(node.incoming)]
        node.outgoing = [i for i in traverse(node.outgoing)]
    
    #adjusting the weights and the probabilities based on the merge
    for k in nodesList:
        if len(k.outgoing)>1:
            totalOutgoingWeight = 0
            for a in k.outgoing:
                totalOutgoingWeight = totalOutgoingWeight + a.weight
        
            for p in k.outgoing:
                for q in k.outgoing:
                    if p.nodeTo == q.nodeTo and p!=q:
                        p.setWeight(q.weight)
                        p.nodeTo.removeIncomingEdge(q)
                        p.nodeFrom.removeOutgoingEdge(q)
                        edgesList.remove(q) 
            
            for j in k.outgoing:
                j.setProbability(float(round(float(j.weight)/totalOutgoingWeight,2)))
        
        elif len(k.outgoing)==1:
            k.outgoing[0].setProbability(1)
    #uncomment if you want to see the list of nodes and edges-the circuit-after every merge
    
    return nodesList,edgesList


# In[74]:

def modelLikelihood(node,circuitString,counter,number,numberList):
    if counter== len(circuitString) and node.state == 'f':
        print 'Model Likelihood:',number
        numberList.append(number)
    
    #Checks every edge and every node - adds transition and output probabilities and becomes recursive to delve into branches
    for edge in node.outgoing:
        if counter == len(circuitString) and edge.nodeTo.state == 'f':
            modelLikelihood(edge.nodeTo, circuitString, counter, number*edge.prob, numberList)

        if counter<len(circuitString):
            if circuitString[counter] in edge.nodeTo.output.keys():
                modelLikelihood(edge.nodeTo, circuitString, counter+1, number*edge.prob*edge.nodeTo.output[circuitString[counter]], numberList)
                continue
    numberList = [sum(numberList)]
    return numberList


# In[75]:

import copy
import math

def chooseNodes(circuitList,nodesList,edgesList):
    mergedNodesList = None
    mergedEdgesList = None
    maxLogValue = -100
    maxLogMerge = []
    nodeStates = []
    for node in nodesList:
        if node.state!='i'and node.state!='f':
            nodeStates.append(node.state)

    for i in nodeStates:
        for g in nodesList:
            if g.state == i:
                nodeI = g
        #o = i + 1
        #while o<= max(nodeStates):
        for o in range(i+1,max(nodeStates)+1):
            if o not in nodeStates:
                continue
            for h in nodesList:
                if h.state == o:
                    nodeO = h
                    
            #print 'OUTSIDE:','i',i,'o',o
            if o in nodeStates and nodeO.output != nodeI.output:
                continue
            
            if o in nodeStates and nodeO.output == nodeI.output:
            #if o in nodeStates:
                a = [nodesList,edgesList]
                b = copy.deepcopy(a)
                nodesListCopy = b[0]
                edgesListCopy = b[1]
                nodes,edges = merge2Nodes(i,o,nodesListCopy,edgesListCopy)
                circuitNum = 1
                for circuitString in circuitList:
                    for k in nodes:
                        if k.state == 'i':
                            initialNode = k
                    count  = 0
                    num = 1
                    myNumberList = []
                    print 'Model Likelihood for', circuitString
                    myNumberList = modelLikelihood(initialNode,circuitString,count,num,myNumberList)
                    #print 'myNumberList',myNumberList
                    print 'circuitNum:',circuitNum
                    for number in myNumberList:
                        circuitNum = circuitNum*number
                    if circuitNum<=0:
                        continue
                    else:
                        pass
                    logValue = math.log(circuitNum,10)
                    print 'Log value', logValue
                    if circuitString == circuitList[-1]:
                        if logValue>maxLogValue:
                            maxLogValue = logValue
                            mergedNodesList = nodes
                            mergedEdgesList = edges
                            nodeState1 = i
                            nodeState2 = o

           
    if mergedNodesList==None and mergedEdgesList==None:
        print 'None'
        print 'NODES', len(nodesList)            
        for j in nodesList:
            print 'Output:',j.output,' State:',j.state, 'Node'
            for k in j.incoming:
                print 'Incoming:','from:', k.nodeFrom.state,k.nodeFrom.output,'to:',k.nodeTo.state,k.nodeTo.output
            for l in j.outgoing:
                print 'Outgoing:', 'from:',l.nodeFrom.state,l.nodeFrom.output,'to',l.nodeTo.state,l.nodeTo.output    
            print ''
        print ''

        print 'EDGES',len(edgesList)     
        for k in edgesList:
            print 'Probability:',k.prob,'Weight:',k.weight, 'Node from:',k.nodeFrom.output,k.nodeFrom.state,'Node to:',k.nodeTo.output,k.nodeTo.state
        print 
        return maxLogValue,nodesList,edgesList

    elif mergedNodesList!=None and mergedEdgesList!=None:
        print 'FINAL',maxLogValue ,nodeState1,nodeState2
        print 'NODES',len(nodesList)         
        for j in mergedNodesList:
            print 'Output:',j.output,' State:',j.state, 'Node'
            for k in j.incoming:
                print 'Incoming:','from:', k.nodeFrom.state,k.nodeFrom.output,'to:',k.nodeTo.state,k.nodeTo.output
            for l in j.outgoing:
                print 'Outgoing:', 'from:',l.nodeFrom.state,l.nodeFrom.output,'to',l.nodeTo.state,l.nodeTo.output    
            print ''
        print ''

        print 'EDGES',len(edgesList)     
        for k in mergedEdgesList:
            print 'Probability:',k.prob,'Weight:',k.weight, 'Node from:',k.nodeFrom.output,k.nodeFrom.state,'Node to:',k.nodeTo.output,k.nodeTo.state
        print 
        return maxLogValue,mergedNodesList,mergedEdgesList


# In[76]:

#final executing function: the nodes and edges list are inputted and it keeps merging to get the final merged model
def keepMerging(circuitList,nodesList,edgesList,threshold):
    preMaxLogValue=0
    maxLogValue,nodesList,edgesList = chooseNodes(circuitList,nodesList,edgesList)
    print 'preMaxLogValue:',preMaxLogValue,'maxLogValue:',maxLogValue
    
    #so that jump from one merge to another is never too great - never above the threshold
    while preMaxLogValue - maxLogValue<threshold:
        preMaxLogValue,preNodesList,preEdgesList = maxLogValue,nodesList,edgesList
        maxLogValue,nodesList,edgesList = chooseNodes(circuitList,nodesList,edgesList)
    
    #if the preMaxLogValue and preNodes, preEdges list have never been equated to maxLogValue, nodes, edges list 
    #because the first merge before the while already made the preMaxLogValue - maxLogValue>= threshold value
    if preMaxLogValue==0:
        return maxLogValue,nodesList,edgesList
    
    #otherwise we remain with the preMaxLogValue, preNodesList etc because that is the circuit before the merging exceeded the threshold
    else:
        return preMaxLogValue,preNodesList,preEdgesList


# In[77]:

def inputNew(nodesListModel,edgesListModel, nodesListNew, edgesListNew):
    #introduce i nodes for input and merged models
    for i in nodesListNew:
        if i.state=='i':
            currentNodeNew = i
    for i in nodesListModel:
        if i.state=='i':
            currentNodeModel = i
    
    probability = 1
    
    #keep going until you reach the last node in the new inputted model
    while currentNodeNew.state!='f':
        
        #iterate through the various outgoing edges of the merged model
        for edgeModel in currentNodeModel.outgoing:
            
            #we need nested if statements because if we are going to the final node, the output dictionary will be empty
            #so it will show an error if I say output.keys()[0]
            if currentNodeNew.outgoing[0].nodeTo.output!={}:
                if currentNodeNew.outgoing[0].nodeTo.output.keys()[0] in edgeModel.nodeTo.output:
                
                #add transition probability and output probability
                    probability = probability * edgeModel.prob
                    probability = probability * edgeModel.nodeTo.output[currentNodeNew.outgoing[0].nodeTo.output.keys()[0]]
                    currentNodeModel = edgeModel.nodeTo
                    currentNodeNew = currentNodeNew.outgoing[0].nodeTo
                elif currentNodeNew.outgoing[0].nodeTo.output.keys()[0] not in edgeModel.nodeTo.output:
                    return 'The new inputted circuit can NOT be produced by the merged model'

            
            #if we are going to the final node then we can't have output probabilities. 
            #This will also be the end of the input circuit so we return at the end
            elif currentNodeNew.outgoing[0].nodeTo.state=='f'and edgeModel.nodeTo.state=='f':
                probability = probability * edgeModel.prob
                currentNodeModel = edgeModel.nodeTo
                currentNodeNew = currentNodeNew.outgoing[0].nodeTo
                return 'Probability of Input model being outputted', probability


# In[78]:

import ast #to convert the text file of lists to real lists
import re #import regex - regular expressions

def convertCircuitList(fileSource):
    listOfCircuits  = ast.literal_eval(open(fileSource).read())
    if any(isinstance(el, list) for el in listOfCircuits)==False:
        listOfCircuits = [listOfCircuits]
    for sublist in listOfCircuits:
        for substring in sublist:
            if type(substring)==str:
                #series of if statements and regex to check which transcriptional unit (?) it is and make a dict with label
                if re.match(r"p\S+", substring):
                    listOfCircuits[listOfCircuits.index(sublist)][sublist.index(substring)] = {substring:"promoter"}
                elif re.match(r"\S+J\d*", substring):
                    listOfCircuits[listOfCircuits.index(sublist)][sublist.index(substring)] = {substring:"ribozyme"}
                elif re.match(r"(BM3R1)|([A-Z][a-z]+[A-Z])", substring):
                    listOfCircuits[listOfCircuits.index(sublist)][sublist.index(substring)] = {substring:"CDS"}
                elif re.match(r"(ECK)|(L3S)\S+", substring):
                    listOfCircuits[listOfCircuits.index(sublist)][sublist.index(substring)] = {substring:"terminator"}
                elif re.match(r"[A-Z]\d", substring):
                    listOfCircuits[listOfCircuits.index(sublist)][sublist.index(substring)] = {substring:"ribosome_entry_site"}
    return listOfCircuits


# In[79]:

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
    return sequenceOfParts


# In[ ]:

#all good circuits for PRRCT
goodTrainingCircuits = convertCircuitList("/Users/Kaveri/Documents/RISE/Data_of_circuits/good_circuits_subset_training.txt")
goodTrainingPRRCT = breakingUpCircuits(["promoter", "ribozyme", "ribosome_entry_site", "CDS", "terminator"], goodTrainingCircuits)
#flattening the list of lists of lists into a list of lists
goodTrainingPRRCT = [item for sublist in goodTrainingPRRCT for item in sublist]

nodesListGoodTrainingPRRCT, edgesListGoodTrainingPRRCT = createInitialModel(goodTrainingPRRCT)
maxLogValuePRRCT, nodesListModelPRRCT, edgesListModelPRRCT = keepMerging(goodTrainingPRRCT, nodesListGoodTrainingPRRCT, edgesListGoodTrainingPRRCT,20)

#test set
goodTestCircuits = convertCircuitList("/Users/Kaveri/Documents/RISE/Data_of_circuits/good_circuits_subset_test.txt")
goodTestPRRCT = breakingUpCircuits(["promoter", "ribozyme", "ribosome_entry_site", "CDS", "terminator"], goodTestCircuits)
goodTestPRRCT = [item for sublist in goodTestPRRCT for item in sublist]
nodesListGoodTestPRRCT,edgesListGoodTestPRRCT = createInitialModel(goodTestPRRCT)

#check probability of test circuit being created by training set
#inputNew(nodesListGoodTrainingPRRCT, edgesListGoodTrainingPRRCT, nodesListGoodTestPRRCT,edgesListGoodTestPRRCT)

inputNew(nodesListModelPRRCT, edgesListModelPRRCT, nodesListGoodTestPRRCT,edgesListGoodTestPRRCT)


# In[ ]:



