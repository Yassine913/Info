def read_file(path):
    f=open(path,'r')
    l=list()
    for line in f:
        word=line[0:len(line)-1]
        if len(word)<=8:
            l.append(word)
    f.close()
    return l

def is_word_possible(word,tirage):
    l=list(word)
    t=tirage.copy()
    for j in word:
        if j in t:
            t.remove(j)
            l.remove(j)
    if l==[]:
        return True
    else:
        return False

def possiblewords(tirage,path):
    return [word for word in read_file(path) if is_word_possible(word,tirage)]
def Longestword(tirage,path):
    wordpossible=possiblewords(tirage,path)
    i=0
    solution=wordpossible[0]
    while i<len(wordpossible)-1:
        i+=1
        if len(wordpossible[i])>len(solution):
            solution=wordpossible[i]
    return solution
        

    
    