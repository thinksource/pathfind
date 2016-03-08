import unittest
from arrayio import *
from pathfind import *

caseA='''46B E59  EA C1F 45E  63
    899 FFF 926 7AD C4E FFF
    E2E 323 6D2 976 83F C96
    9E9 A8B 9C1 461 F74 D05
    EDD E94 5F4 D1D D03 DE3
     89 925 CF9 CA0 F18 4D2
'''
pathA=[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3), (3, 4), (4, 4), (5, 4), (5, 5)]
simpleA= [[2,5,7,3,5,2],[1,9,2,1,8,3],[1,1,3,3,1,8],
   [2,1,1,3,8,9],[1,3,1,3,9,6],[4,2,8,7,2,4]]
valueA=[[1131, 3673, 234, 3103, 1118, 99], [2201, 4095, 2342, 1965, 3150, 4095], [3630, 803, 1746, 2422, 2111, 3222], [2537, 2699, 2497, 1121, 3956, 3333], [3805, 3732, 1524, 3357, 3331, 3555], [137, 2341, 3321, 3232, 3864, 1234]]
class TestpathFind(unittest.TestCase):
    def setUp(self):
        self.startx=0
        self.starty=0
        self.endx=5
        self.endy=5
        self.inA=input_array(caseA)

    def test_example(self):
        ps=Astarsearch(self.startx,self.starty,self.endx, self.endy,self.inA)
        ps.find_path()
        self.assertEqual('r,r,d,d,r,d,d,r,r,d',ps.printway())

    def test_cost(self):
        ps=Astarsearch(self.startx,self.starty,self.endx, self.endy,self.inA)
        self.assertEqual(ps.cost(0,0,1,0),2402)
        self.assertEqual(ps.cost(0,1,1,1),3148)

    def test_findpath(self):
        ps=Astarsearch(self.startx,self.starty,self.endx, self.endy,self.inA)
        self.assertEqual(ps.find_path(),pathA)

    def test_simple(self):
        startx=1
        starty=0
        endx=5
        endy=5
        path=[(1, 0), (0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (5, 5)]
        ps=Astarsearch(startx,starty,endx, endy,simpleA)
        self.assertEqual(path, ps.find_path())
    def test_arrayio(self):
        self.assertEqual(valueA,self.inA)
        
    def test_Node(self):
        nodeA=Node(0,1,0.0,None)
        nodeA.setpriority(1)
        nodeB=Node(0,0,1.0,None)
        nodeB.setpriority(0)
        self.assertTrue(nodeA>nodeB)

if __name__ == '__main__':
    unittest.main()
