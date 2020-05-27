
# In[ ]:


import pygame
import math
import sys
import numpy as np
import time

# In[ ]:


st=time.clock()
print("\t\tDijkstra's Algorithm\n")
print("Enter initial node cordinates")
xi=float(input("x =  "))
yi=float(input("y =  "))
init_node=[xi,yi]
print("Enter goal node cordinates (max 230x144 )")
xg=float(input("x =  "))
yg=float(input("y =  "))
goal=[xg,yg]
r=int(input("Enter Resolution (must be an integer value) =  "))
sd=0;
goal= [n / r for n in goal]
init_node=[m / r for m in init_node]

rows=144/r
coloums=230/r


# In[ ]:


def left(current_node):
    next_node=[0,0]
    next_node[0]=current_node[0]-1
    next_node[1]=current_node[1]
    cost=1
    
    return next_node,cost

def right(current_node):
    next_node=[0,0]
    next_node[0]=current_node[0]+1
    next_node[1]=current_node[1]
    cost=1
    
    return next_node,cost

def down(current_node):
    next_node=[0,0]
    next_node[0]=current_node[0]
    next_node[1]=current_node[1]+1
    cost=1
        
    return next_node,cost

def up(current_node):
    next_node=[0,0]
    next_node[0]=current_node[0]
    next_node[1]=current_node[1]-1
    cost=1
    
    return next_node,cost

def down_left(current_node):
    next_node=[0,0]
    next_node[0]=current_node[0]-1
    next_node[1]=current_node[1]+1
    cost=1.42
    
    return next_node,cost

def up_left(current_node):
    next_node=[0,0]
    next_node[0]=current_node[0]-1
    next_node[1]=current_node[1]-1
    cost=1.42
    
    return next_node,cost
                  
def up_right(current_node):
    next_node=[0,0]
    next_node[0]=current_node[0]+1
    next_node[1]=current_node[1]-1
    cost=1.42
    
    return next_node,cost
                  
def down_right(current_node):
    next_node=[0,0]
    next_node[0]=current_node[0]+1
    next_node[1]=current_node[1]+1
    cost=1.42
    
    return next_node,cost
def obstacle_space(x,y,r):
    c = 0
    #big circle
    if ((x-math.ceil(140/r))**2+math.ceil(y-(120/r))**2-math.ceil(15/r)**2)<=0:
        c=1
    #rhombus    
    if (38*x- 7*y - 5830/r >= 0) and (38*x + 23*y - 8530/r <= 0) and (37*x -20*y -6101/r <= 0) and (37*x +10*y - 6551/r >= 0):
   	c=1
    ##parallelogram
    if (2*x + 19*y - 2514/r <= 0) and (41*x+ 25*y -5300/r >= 0) and (y - 90/r>= 0) and (37*x +10*y - 5000/r <= 0):
        c=1
    #rect1
    if (x-math.floor(20/r) >= 0) and (x - math.floor(40/r) <= 0) and (y - math.floor(67.5/r) >= 0) and (y - math.floor(112.5/r) <= 0):
        c=1
    #rect2
    if (x-math.floor(90/r) >= 0) and (x - math.floor(155/r) <= 0) and (y - math.floor(55/r) >= 0) and (y - math.floor(74/r) <= 0):
        c=1    
    #ovaltop 
    if ((x-math.ceil(186/r))/math.ceil(15/r))**2 + ((y - math.ceil(106/r))/math.ceil(6/r))**2 - 1 <=0:
        c=1
    #oval bottom
    if ((x-math.ceil(70/r))/math.ceil(19/r))**2 + ((y - math.ceil(39/r))/math.ceil(12/r))**2 - 1 <=0:
        c=1
    return c
    
        

p_nd=[init_node]
c_nd=[init_node]
vp_nd=[]
visited_node=[]
v_cst=[]
if (obstacle_space(goal[0],goal[1],r)==1 or obstacle_space(init_node[0],init_node[1],r)):
    sys.exit("Either goal node or start node lies inside obstacle ")

if (init_node[0] not in range(0,231) or goal[0] not in range(0,231) or init_node[1] not in range(0,145) or goal[1] not in range(0,145)):
    sys.exit("Entered node cordinates are not integers or outside the workspace or invalid resolution")



# In[ ]:



x=0
cst=[0]
ndx=init_node
flag=0

while(flag!=1):
    
    #goes up
    nd,cost=up(ndx)
    if (nd[1]>=0 and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in visited_node:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))
        
 
            
    #to go down
    nd,cost=down(ndx)
    if (nd[1]<=rows and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in visited_node:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))

            
    #to go left
    nd,cost=left(ndx)
    if (nd[0]>=0 and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in visited_node:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))


    #to go right
    nd,cost=right(ndx)
    if (nd[0]<=coloums and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in visited_node:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))

            
    #north west
    nd,cost=up_left(ndx)
    if (nd[1]>=0 and nd[0]>=0 and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in visited_node:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))

            
    #north east
    nd,cost=up_right(ndx)
    if (nd[0]<=coloums and nd[1]>=0 and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in visited_node:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))


            
    #south west
    nd,cost=down_left(ndx)
    if (nd[1]<=rows and nd[0]>=0 and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in visited_node:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))
            

                    
    #south east
    nd,cost=down_right(ndx)
    if (nd[1]<=rows and nd[0]<=coloums and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in visited_node:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))

        
                    
    vp_nd.append(p_nd.pop(x))
    visited_node.append(c_nd.pop(x))
    v_cst.append(cst.pop(x))
    
    
    if(visited_node[-1]==goal):
        flag=1
        
    if(flag!=1):
        x=cst.index(min(cst))
        ndx=c_nd[x][:]

seq=[]
seq.append(visited_node[-1])
seq.append(vp_nd[-1])
x=vp_nd[-1]
i=1
while(x!=init_node):
    if(visited_node[-i]==x):
        seq.append(vp_nd[-i])
        x=vp_nd[-i]
        sd+=1
    i=i+1      


# In[ ]:


obs_space = []
for i in range(0,231):
    for j in range(0,145):
        q=obstacle_space(i,j,r)
        if q == 1:
            obs_space.append([i,j])

k=2
my_list = np.array(visited_node)
visited_node=my_list*k*r
my_list1 = np.array(seq)
seq=my_list1*k*r
my_list2 = np.array(obs_space)
obs_space = my_list2*k*r


pygame.init()

Black = [0, 0, 0]
grey = [192, 192, 192]
Blue = [0, 100, 255]
White = [255, 255, 255]
red= [200, 0, 0]

#length and breadth
SIZE = [230*k+r+r, 144*k+r+r]
screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption("Dijkstra's algorithm")
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            done = True    
 
    screen.fill(White)
#print the obstacles
    for i in obs_space:
        pygame.draw.rect(screen, red, [i[0],144*k-i[1],r*k,r*k])
    pygame.display.flip()
    clock.tick(20)
#print the visited nodes(shows how everything is getting scanned)
    for i in visited_node:
        pygame.time.wait(1)
        pygame.draw.rect(screen, Black, [i[0],144*k-i[1],r*k,r*k])
        pygame.display.flip()
#print the path
    for j in seq[::-1]:
        pygame.time.wait(1)
        pygame.draw.rect(screen, grey, [j[0], 144*k-j[1], r*k,r*k])
        pygame.display.flip()
    pygame.display.flip()

    pygame.time.wait(8000)
    done = True
pygame.quit()

et=time.clock()
tt=et-st
print("Total distance moved is %d"%sd)
print('Total time taken by Dijkstras algorithm is %.4fs'%tt)
