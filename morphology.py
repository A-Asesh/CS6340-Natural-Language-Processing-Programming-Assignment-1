import sys
file_dictionary = sys.argv[1]
file_rules = sys.argv[2]
file_test = sys.argv[3]

#-------------------------------------------------------------------------
def Morphology(i,original,check,pos,indexOfWord):
    checkword=''.join(i)
    flag=True
    for r in rules:
        if "suffix" == r[0] and checkword.endswith(r[1]):
            if check==r[4] or check==None:
                flag=False
                testwordcut=checkword[0:len(checkword)-len(r[1])]
                if r[2].isalpha():
                    testwordcut=testwordcut+r[2]
                if testwordcut in maindict and r[3] in maindict[testwordcut]:
                    found_words[indexOfWord].append('T')
                    if pos is None:
                        print(''.join([original+" ",r[4]+" ","ROOT="+testwordcut+" ","SOURCE=Morphology"]))
                    else:
                        print(''.join([original+" ",pos+" ","ROOT="+testwordcut+" ","SOURCE=Morphology"]))
                else:
                    a_rules=r[3]
                    Morphology(testwordcut,original,a_rules,r[4],indexOfWord)
            else:
                checkword=original
                check=None

        elif "prefix" == r[0] and checkword.startswith(r[1]):
            if check==r[4] or check==None:
                flag=False 
                testwordcut=checkword[len(r[1]):]
                if r[2].isalpha():
                    testwordcut=testwordcut+r[2]
                if testwordcut in maindict and r[3] in maindict[testwordcut]:
                    found_words[indexOfWord].append('T')
                    if pos is None:
                        print(''.join([original+" ",r[4]+" ","ROOT="+testwordcut+" ","SOURCE=Morphology"]))
                    else:
                        print(''.join([original+" ",pos+" ","ROOT="+testwordcut+" ","SOURCE=Morphology"]))
                else:
                    a_rules=r[3]
                    Morphology(testwordcut,original,a_rules,r[4],indexOfWord)
            else:
                checkword=original
                check=None
        else:
             testwordcut=original
    return testwordcut,flag
                 
#-------------------------------------------------------------------------              
with open(file_dictionary, 'r') as document:
    maindict = {}
    for line in document:
        line=line.lower()
        line = line.split()
        first=line[0]
        if first in maindict:
            maindict[first].extend(line[1:])
        else:
            maindict[first]=line[1:]
"""for i in maindict:
    print(i,maindict[i])"""

#-------------------------------------------------------------------------
test_array = []
with open(file_test) as my_file:
    for line in my_file:
        line=line.lower()
        line = line.split()
        test_array.append(line)
"""for i in test_array:
    print (i)"""

#-------------------------------------------------------------------------
with open(file_rules, 'r') as document:
    rules = []
    for line in document:
        line=line.lower()
        line = line.split()
        rules.append(line)
  
for i in rules:
    del i[6]
    del i[4]
"""    print(i)"""

#-------------------------------------------------------------------------
found_words=[]
for i in test_array:
    found_words.append(i)

#print found_words
for i in test_array:
    testword=''.join(i)
    if testword in maindict:
            if "ROOT" in maindict[testword]:
                    found_words[test_array.index(i)].append('T')
                    print(''.join([testword+" ",maindict[testword][0]+" ","ROOT="+maindict[testword][maindict[testword].index("root")+1]+" ","SOURCE=Dictionary"]))
            else:
                    found_words[test_array.index(i)].append('T')
                    print(''.join([testword+" ",maindict[testword][0]+" ","ROOT="+testword+" ","SOURCE=Dictionary"]))
    else:
        indexOfWord=test_array.index(i)
        #print indexOfWord
        new_word, flag=Morphology(i,testword,None,None,indexOfWord)
       # if new_word == testword and flag:
        #    print(''.join([testword+" ","noun ","ROOT="+testword+" ","SOURCE=Default"]))

#print found_words

for i in found_words:
    if len(i)==1 and flag==False:
        print ''.join(i[0]),"noun","ROOT="+i[0],"SOURCE=Default"
#-------------------------------------------------------------------------
