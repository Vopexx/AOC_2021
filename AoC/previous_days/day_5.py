

day = 5
f = open("inputs/inputd-"+str(day)+".txt", "r")
contenu = f.read().split("\n")[:-1]


segments = []
for i in contenu:
    segments.append([ [*map(int,j.replace(" ","").split(","))] for j in i.split("->")])

#--------------- PROG :


all_points = []

for i in range(1000):
    all_points.append([0]*1000)


for segment in segments:  #segments = [ [ [X, X], [X, X] ] , ...]
    p1, p2 = segment  # segment = [ [ X, X ] , [ X, X ] ]
    x1,y1 = p1
    x2,y2 = p2

    if x1==x2:
        for x in range(min(y1,y2), max(y1,y2)+1):



            all_points[x1][x] += 1 

    else:    
        m = int((y1 - y2) / (x1 - x2))
        low = min(x1,x2)
        big = max(x1,x2)
        if m==0:
            for x in range(low, big+1):


                
                all_points[x][y1] += 1 

        else:
            #part1 --> "continue" / part2 --> " "
            y = [y2,y1][low==x1] - m  # + m avoid forgetting first point of the diagonal
            for x in range(low, big+1):
                y += m

                all_points[x][y] += 1 



c=0
for j in sorted(all_points):
    for i in j:
        if i > 1:

            c+=1
print(c)
