import numpy as np
def table(data,k=4):
    t={}
    for i in range(len(data)-k):
        x=data[i:i+k]
        y=data[i+k]
        
        
        if t.get(x) is None:
            t[x]={}
            t[x][y]=1
        else:
            if t[x].get(y) is None:
                t[x][y]=1
            else:
                t[x][y]+=1

    return t        

def convert(t):
    for kx in t.keys():
        s=sum(t[kx].values())
        for k in t[kx].keys():
            t[kx][k]=t[kx][k]/s
    return t
def train(text,k=4):
    t=table(text)
    t=convert(t)
    return t
         

text=open('ml.txt','r')
train(text)

 
 
