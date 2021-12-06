
day = 3



f = open("inputs/inputd-"+str(day)+".txt", "r")
contenu = f.read().split("\n")[:-1]



#--------------- PROG :


        
contenu1, contenu2 = contenu, contenu
for i in range(len(contenu[0])):

    
    if len(contenu1) > 1:
        
        y = list(zip(*contenu1))[i]     
        most = str(int(y.count("1") >= y.count("0")))  
        c = [j for j, x in enumerate(y) if x == most]
        contenu1 = [contenu1[j] for j in c]
        
    if len(contenu2) > 1:
        z = list(zip(*contenu2))[i]
        less = str(int(z.count("1") >= z.count("0"))^1)
        d = [j for j, x in enumerate(z) if x == less]
        contenu2 = [contenu2[j] for j in d]
    
print(int(contenu1[0],2),int(contenu2[0],2))

        
