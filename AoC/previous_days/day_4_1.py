
day = 4



f = open("inputs/inputd-"+str(day)+".txt", "r")
contenu = f.read().split("\n\n")





for _ in range(len(contenu)):
    if _ == len(contenu) - 1 :
        contenu[_] = [j.split() for j in contenu[_].split("\n")[:-1]]
    else:
        contenu[_] = [j.split() for j in contenu[_].split("\n")]
#--------------- PROG :
print(contenu)
search = contenu[0][0][0].split(",")
content = contenu[1:]






def searching(contenu, search):
    # contenu = Block
    # row
    for j in contenu: # j = [X,X,X,X,X]
        trouver = True
        for k in j: # k = X

            if not (k in search):
                trouver = False
        if trouver:
            return trouver
    

    # column
    for j in zip(*contenu): # j = [X,X,X,X,X]
        trouver = True
        for k in j: # k = X

            if not (k in search):
                trouver = False
        if trouver:
            return trouver
    return False

v=0
stop = False
while not stop:
    v+=1
    s = search[:v] 
    
    for i in content: # i = [ [X,X,X,X,X], [X,X,X,X,X], [X,X,X,X,X], [X,X,X,X,X], [X,X,X,X,X] ]
        if searching(i, s):
            block = i
            stop = True
            break


print(block,"\n",s)
print(sum([sum([int(j) for j in i if not (j in s)]) for i in block])*int(s[-1]))

