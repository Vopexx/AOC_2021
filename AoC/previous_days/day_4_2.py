
day = 4



f = open("inputs/inputd-"+str(day)+".txt", "r")
contenu = f.read().split("\n\n")


for _ in range(len(contenu)):
    if _ == len(contenu) - 1 :
        contenu[_] = [j.split() for j in contenu[_].split("\n")[:-1]]
    else:
        contenu[_] = [j.split() for j in contenu[_].split("\n")]

#--------------- PROG :

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
            maxi = 0
            b=j
            for m in b:
                d = search.index(m)
                if d > maxi:
                    maxi = d

            elem = search[maxi]
            o = sum([sum([int(p) for p in w if not (p in search[:maxi+1])])for w in contenu])
            list_win.append((maxi,o*int(elem)))
            #return trouver, j
    

    # column
    for j in zip(*contenu): # j = [X,X,X,X,X]

        trouver = True
        for k in j: # k = X

            if not (k in search):
                trouver = False
        if trouver:
            maxi = 0
            b=j
            for m in b:
                d = search.index(m)
                if d > maxi:
                    maxi = d

            elem = search[maxi]
            o = sum([sum([int(p) for p in w if not (p in search[:maxi+1])])for w in contenu])
            list_win.append((maxi,o*int(elem)))



list_win = []
board_fucked = []
for i in content: # i = [ [X,X,X,X,X], [X,X,X,X,X], [X,X,X,X,X], [X,X,X,X,X], [X,X,X,X,X] ]
    searching(i, search)
print(sorted(list_win))

print(sorted(list_win))
c=[]      
z=[]


for j in sorted(list_win):
    
    if c.count(j[1]) < 1:
        z.append(j)
        c.append(j[1])

print(z)