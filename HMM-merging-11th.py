
# coding: utf-8

# In[21]:

#class Node creates nodes with properties state, edge, incoming, outgoing
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
    def setProbability(self, prob):
        self.prob = prob
    def setNodeFrom(self, nodeFrom):
        self.nodeFrom = nodeFrom  
    def setNodeTo(self,nodeTo):
        self.nodeTo = nodeTo  
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

    print 'Nodes', len(nodesList)        
    for j in nodesList:
        print 'Output:',j.output,' State:',j.state, 'Node'
        for k in j.incoming:
            print 'Incoming:','from:',k, k.nodeFrom.state,k.nodeFrom.output,'to:',k.nodeTo.state,k.nodeTo.output
        for l in j.outgoing:
            print 'Outgoing:', 'from:',l, l.nodeFrom.state,l.nodeFrom.output,'to',l.nodeTo.state,l.nodeTo.output    
        print 
    
    print 'Edges', len(edgesList)
    for k in edgesList:
        print k,'Probability:',k.prob,'Weight:',k.weight, 'Node from:',k.nodeFrom.output,k.nodeFrom.state,'Node to:',k.nodeTo.output,k.nodeTo.state
    print ''
    return nodesList,edgesList

createInitialModel([['a','b'],['a','b','a','b']])


# In[22]:

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
    
    if node1.output != node2.output:
        return
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
    
    for i in node1.incoming:
        if node1.incoming.index(i)<= len(node2.incoming):
                node2Incoming = Edge()
                node2Incoming.setNodeTo(node1)
                node2Incoming.setNodeFrom(node2.incoming[0].nodeFrom)
                edgesList.append(node2Incoming)
                node1.addIncomingEdge(node2Incoming)
                node2.incoming[0].nodeFrom.addOutgoingEdge(node2Incoming)
                node2.incoming[0].nodeFrom.removeOutgoingEdge(node2.incoming[0])
                node2.removeIncomingEdge(node2.incoming[0])

    #adding a new outgoing edge to node1 IF node 1 and node 2 don't go to the same node
    print ''
    for j in node1.outgoing:
        if node1.outgoing.index(j)<= len(node2.outgoing):
                node2Outgoing = Edge()
                node2Outgoing.setNodeFrom(node1)
                node2Outgoing.setNodeTo(node2.outgoing[0].nodeTo)
                edgesList.append(node2Outgoing)
                node1.addOutgoingEdge(node2Outgoing)
                node2.outgoing[0].nodeTo.addIncomingEdge(node2Outgoing)
                node2.outgoing[0].nodeTo.removeIncomingEdge(node2.outgoing[0])
                node2.removeOutgoingEdge(node2.outgoing[0])
    
    nodesList.remove(node2)
    for node in nodesList:
        node.incoming = [i for i in traverse(node.incoming)]
        node.outgoing = [i for i in traverse(node.outgoing)]
    
    #calculation of probabilities using weights
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
    #printing nodes and edge lists
    print 'Nodes', len(nodesList)        
    for j in nodesList:
        print 'Output:',j.output,' State:',j.state, 'Node'
        for k in j.incoming:
            print 'Incoming:','from:', k.nodeFrom.state,k.nodeFrom.output,'to:',k.nodeTo.state,k.nodeTo.output
        for l in j.outgoing:
            print 'Outgoing:', 'from:',l.nodeFrom.state,l.nodeFrom.output,'to',l.nodeTo.state,l.nodeTo.output    
        print ''
    print ''
    
    print 'Edges', len(edgesList)
    for k in edgesList:
        print 'Probability:',k.prob,'Weight:',k.weight, 'Node from:',k.nodeFrom.output,k.nodeFrom.state,'Node to:',k.nodeTo.output,k.nodeTo.state
    print ''
    return nodesList,edgesList
mergedNodesList,mergedEdgesList  = createInitialModel([['a','b'],['a','b','a','b']])
merge2Nodes(1,3,mergedNodesList,mergedEdgesList)


# In[23]:

def modelLikelihood(node,circuitString,counter,number,numberList):
    if counter== len(circuitString) and node.state == 'f':

        #number  = number*edge.prob*edge.nodeTo.output[circuitString[counter]]
        print 'Model Likelihood:',number
        numberList.append(number)
        
    for edge in node.outgoing:
        if counter == len(circuitString) and edge.nodeTo.state == 'f':
#calling recursively- multiplying only transition probabilities
            modelLikelihood(edge.nodeTo, circuitString, counter, number*edge.prob, numberList)

        if counter<len(circuitString):
            if circuitString[counter] in edge.nodeTo.output.keys():

#calls function and multiplies the transition and emission probabilities
                modelLikelihood(edge.nodeTo, circuitString, counter+1, number*edge.prob*edge.nodeTo.output[circuitString[counter]], numberList)
                continue
    numberList = [sum(numberList)]
    #print 'Number List in func', numberList
    return numberList


# In[33]:

#choose nodes function
import copy
import math

def chooseNodes(circuitList,nodesList,edgesList):
    maxLogValue = -100
    maxLogMerge = []
    nodeStates = []
    
    for node in nodesList:
        if node.state!='i'and node.state!='f':
            nodeStates.append(node.state)
#nested for loop - finding permutations
    for i in nodeStates:
        for g in nodesList:
            if g.state == i:
                nodeI = g
        o = i + 1
        while o<= max(nodeStates):
            for h in nodesList:
                if h.state == o:
                    nodeO = h
            if o in nodeStates and nodeO.output == nodeI.output:
                
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

#calling model likelihood function
                    myNumberList = modelLikelihood(initialNode,circuitString,count,num,myNumberList)
                    #print 'myNumberList',myNumberList
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
            o = o+1
    nodeStates.remove(nodeState2)
    print 'Max log value:',maxLogValue ,'Node 1:',nodeState1,', Node 2',nodeState2
    print ''
    return maxLogValue,nodeState1,nodeState2,mergedNodesList,mergedEdgesList


# In[34]:

#keep merging function
def keepMerging(circuitList,nodesList,edgesList):
    preMaxLogValue=0
    maxLogValue,nodeState1,nodeState2,nodesList,edgesList = chooseNodes(circuitList,nodesList,edgesList)
    #threshold value for while loop
    while maxLogValue>-4:
        print 'preMaxLogValue',preMaxLogValue
        preMaxLogValue,preNodeState1,preNodeState2,preNodesList,preEdgesList = maxLogValue,nodeState1,nodeState2,nodesList,edgesList
        maxLogValue,nodeState1,nodeState2,nodesList,edgesList = chooseNodes(circuitList,nodesList,edgesList)
    #if the last maxLogValue is smaller than the threshold, the penultimate value is used
    if maxLogValue<-4:
        return preMaxLogValue,preNodeState1,preNodeState2,preNodesList,preEdgesList
    
    elif maxLogValue>=-4:
        return maxLogValue,nodeState1,nodeState2,nodesList,edgesList



# In[11]:


myCircuitList = [["pSrpR","pAmtR","RiboJ53","P3","PhlF","ECK120033737","pBM3R1","RiboJ10","S2","SrpR","ECK120019600","pBAD","pHlyIIR","SarJ","B3","BM3R1","L3S3P11","pTet","pHlyIIR","RiboJ57","E1","BetI","L3S3P11","pBAD","pTet","RiboJ51","H1","HlyIIR","ECK120033736","pTac","BydvJ","A1","AmtR","L3S2P55"],
["pTac","RiboJ53","P2","PhlF","ECK120033737","pBAD","RiboJ10","S1","SrpR","ECK120019600","pSrpR","pHlyIIR","SarJ","B2","BM3R1","L3S3P11","pPhlF","pAmtR","RiboJ57","E1","BetI","L3S3P11","pBetI","RiboJ51","H1","HlyIIR","ECK120033736","pTet","BydvJ","A1","AmtR","L3S2P55"],
["pSrpR","pBetI","RiboJ53","P3","PhlF","ECK120033737","pTac","pTet","RiboJ10","S3","SrpR","ECK120019600","pHlyIIR","pAmeR","RiboJ57","E1","BetI","L3S3P11","pTet","RiboJ54","F1","AmeR","L3S3P31","pTac","RiboJ51","H1","HlyIIR","ECK120033736","pBAD","BydvJ","A1","AmtR","L3S2P55"]]
nodesList2,edgesList2 = createInitialModel(myCircuitList)
keepMerging(myCircuitList,nodesList2,edgesList2)


# In[37]:

#calling function
myCircuitList = [['a','b','c'],['a','b','a','b'], ['a','b','d','b']]  
nodesListA,edgesListA = createInitialModel(myCircuitList)
keepMerging(myCircuitList,nodesListA,edgesListA)


# In[ ]:



