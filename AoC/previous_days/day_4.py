
day = 4


f = open("inputs/inputd-"+str(day)+".txt", "r")

contenu = f.read()[:-1].split("\n\n")


for _ in range(1,len(contenu)):
    
    #contenu[_] = [set(map(int,j.split())) for j in contenu[_].split("\n")]
    
    f=[]
    block = [j.split() for j in contenu[_].split("\n")]
    for j in block:
        f.append(set(map(int,j)))

    for j in zip(*block):
        f.append(set(map(int,j)))
    
    contenu[_] = f
#--------------- PROG :

draws = [int(i) for i in contenu[0].split(",")]
blocks = contenu[1:]




list_win = []

draw = set()
while blocks:
    board_removed = []
    current_draw = draws.pop(0)
    draw |= {current_draw}
    
    for block in blocks: # block = [ [X,X,X,X,X], [X,X,X,X,X], [X,X,X,X,X], [X,X,X,X,X], [X,X,X,X,X] ]
        for line in block: # line = [X,X,X,X,X]

            if line <= draw:

                

                o = sum(set.union(*block) - draw)
                list_win.append(o*current_draw)
                
                
                board_removed.append(block)


                break
                
                
    for block in board_removed:

        blocks.remove(block)

        

print(list_win[0],list_win[-1])


            