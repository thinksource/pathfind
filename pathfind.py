import sys

from heapq import heappush, heappop # for priority queue

rate=1

# in this example the heuristic function is not much useful
# but if you the large scala it would be benefit
def heuristic(startx, starty, endx,endy):
    return (abs(startx-endx)+abs(starty-endy))*rate
    # return 0

class Node:

    def __init__(self,x,y,dist,parent):
        self.x=x
        self.y=y
        self.cost=dist
        self.parent=parent
    def __lt__(self, other):
        return self.priority<other.priority
    def setpriority(self,p):
        self.priority=p

class Astarsearch:

    def __init__(self, startx, starty, endx, endy, mapA):
        self.startx=startx
        self.starty=starty
        self.endx=endx
        self.endy=endy
        self.width=len(mapA[0])
        self.height=len(mapA)
        self.map=mapA
        self.open=[]
        self.path=[]

        self.closemap=[[0 for x in range(self.width)] for x in range(self.height)]
        # every open point is max cost initially
        self.openmap=[[sys.maxint for x in range(self.width)] for x in range(self.height)]

    def expendpoint(self, p):
        p.setpriority(p.cost+heuristic(p.x, p.y, self.endx,self.endy))
        if(self.openmap[p.y][p.x]>p.priority):
            if(self.closemap[p.y][p.x]==0):
                self.openmap[p.y][p.x]=p.priority
                heappush(self.open,p)

    # main algorithm function
    def find_path(self):
        n=Node(self.startx,self.starty,0.0,None)

        n.setpriority(heuristic(n.x, n.y, self.endx,self.endy))
        self.openmap[n.y][n.x]=n.cost
        while True:
            self.expendopen(n)
#            if open list is empty will be no solution find
            if not self.open:
                return None
            n=heappop(self.open)
            if(n.x==self.endx and n.y==self.endy):

                self.makepath(n)
                return self.path
            self.closemap[n.y][n.x]=1

    #draw the path
    def makepath(self,p):
        path=[]
        while p:
            path.append((p.x,p.y))
            p=p.parent
        self.path=path[::-1]

    def printway(self):
        tmpway=""
        length=len(self.path)
        pre_x=self.startx
        pre_y=self.starty
        if length>0:
            for i in range (1, length):
                if(pre_x==self.path[i][0] and pre_y+1==self.path[i][1]):
                    tmpway+='d'
                elif(pre_x==self.path[i][0] and pre_y-1==self.path[i][1]):
                    tmpway+='u'
                elif(pre_x+1==self.path[i][0] and pre_y==self.path[i][1]):
                    tmpway+='r'
                elif(pre_x-1==self.path[i][0] and pre_y==self.path[i][1]):
                    tmpway+='l'
                if(self.path[i][0]!=self.endx or self.path[i][1]!=self.endy):
                    tmpway+=','
                pre_x=self.path[i][0]
                pre_y=self.path[i][1]
        return tmpway

    def cost(self, x1,y1,x2,y2):
        return (self.map[y1][x1]+self.map[y2][x2])/2

    # 4 directions step
    def expendopen(self, node):
        #left
        if(node.x-1>=0):
            tmpx=node.x-1
            tmpcost=self.cost(node.x,node.y,tmpx,node.y)
            tmp=Node(tmpx,node.y,node.cost+tmpcost,node)
            self.expendpoint(tmp)
        #right
        if(node.x+1<self.width):
            tmpx=node.x+1
            tmpcost=self.cost(node.x,node.y,tmpx,node.y)
            tmp=Node(tmpx,node.y,node.cost+tmpcost,node)
            self.expendpoint(tmp)
        #up
        if(node.y-1>=0):
            tmpy=node.y-1
            tmpcost=self.cost(node.x, node.y,node.x,tmpy)
            tmp=Node(node.x, tmpy,node.cost+tmpcost,node)
            self.expendpoint(tmp)
        #down
        if(node.y+1<self.height):
            tmpy=node.y+1
            tmpcost=self.cost(node.x, node.y,node.x,tmpy)
            tmp=Node(node.x, tmpy,node.cost+tmpcost,node)
            self.expendpoint(tmp)
