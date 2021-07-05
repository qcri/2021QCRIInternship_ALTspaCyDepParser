import spacy

f = open('test3.txt','r')
fout = open('testout.txt', 'w')

nlp = spacy.load("en_core_web_sm")

l = 0 
from spacy.tokenizer import Tokenizer
import re

for line in f:
    lines = line.strip()
    #print(line)
    if(lines == '-DOCSTART-'):
        print(line)
        fout.write(line+"\n")
        continue
    nlp.tokenizer = Tokenizer(nlp.vocab, token_match=re.compile(r'\S+').match)
    docs = nlp(lines)
    
    for doc in docs:
        
        if doc.ent_type_!= "ORG" and doc.ent_type_!= "PERSON" and doc.ent_type_!= "GPE":
            fout.write('%s %s\n'%(doc.text,"O"))

        elif doc.ent_type_ =="GPE":
            #fout.write('%s %s-%s\n'%(doc.text, doc.ent_iob_,"LOC"))
            fout.write('%s %s\n'%(doc.text,"LOC"))

            
        elif doc.ent_type_ =="PERSON":
            #fout.write('%s %s-%s\n'%(doc.text, doc.ent_iob_,"PER"))
            fout.write('%s %s\n'%(doc.text,"PER"))
            
        
        elif doc.ent_iob_=='O':
            fout.write('%s %s\n'%(doc.text, doc.ent_iob_))
            
        else:
        
            #fout.write('%s %s-%s\n'%(doc.text, doc.ent_iob_,doc.ent_type_))
            fout.write('%s %s\n'%(doc.text,doc.ent_type_))
    #print()
    fout.write("\n")
fout.close()

l = 0 
for line in f:
    line = line.strip()
   
    #print(line)
    if(line == '-DOCSTART-'):
        fout.write(line+"\n\n")
        continue
    
   
    doc = nlp(line)
    if len(doc)>2:
        if "-" in doc.text:
            doc=nlp(line.replace("-","d"))
    for token in doc:
        fout.write('%s %s\n'%(token.text, token.ent_iob_))

    fout.write("\n")

fout.close()

#input file
fin = open("test.txt")
#output file to write the result to
fout = open("testED.txt", "w")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
    words=line.split()
    if len(words)==0:
        fout.write(line)
    elif words[0]=="-DOCSTART-":
        fout.write("-DOCSTART-\n")
    else:
        if words[-1][2:]=="MISC":
            new=words[0]+" "+"O"+"\n"
            
        elif words[-1]=="O":
            new=words[0]+" "+words[-1]+"\n"
        else:
            new=words[0]+" "+words[-1][2:]+"\n"
        fout.write(new)


fout.close()

f=open("testout.txt")
for line in f:
    print(line)

import pandas as pd
#dataout=pd.read_csv("testout.txt",sep=" ")
def loadFile(name):
    dataout=[]
    for line in open(name):
        if "-DOCSTART-" in line:
            continue

        data=line.strip().split()
        if len(data)!=2:
            continue
        dataout.append(data)

    dataout1=pd.DataFrame(dataout)
    dataout1.columns=["Word","Pars"]
    
    return dataout1

testOut=loadFile("testout.txt")
testED=loadFile("testED.txt")

# Import `metrics` from `sklearn`
from sklearn import metrics
# Print the classification report of `y_test` and `y_pred`
print(metrics.classification_report(testED["Pars"], testOut["Pars"]))

# Print the confusion matrix
print(metrics.confusion_matrix(testED["Pars"], testOut["Pars"]))





