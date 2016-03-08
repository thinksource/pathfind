#Assumptions&Reasons:

1, the input number is considered as hexadecimal numbers: for example the 46B will regards the number 1131 in decimal.

2, the cost of from one cell of array to its neighbor is: the number of this cell cost add
the that number of its neighbor and then divided 2.
which is represent the cost function:

```
def cost(self, x1,y1,x2,y2):
    return (self.map[y1][x1]+self.map[y2][x2])/2
```
(it is reasonable to consider the distance caculation by arithmetic mean)
In other words, I use the edge movement caculate method to catulate the cost of movemnet. The cost of the path in each room is not unit, it determine by the tile you came from and the tile you go to.

If you want to use the neil cost, you can use the
```
def cost(self, x1,y1,x2,y2):
    return self.map[y2][x2]
```
That is indicate the every directions the cost is unifrom.

3, the minify number of cost represent the cell is 1(no zero cost), and the cost should be integer number. (I think in the real world the travel distance must be positive cost.)

4, the input numbers must be as array.

5, (bouns)the algorithm will consider allowing the robot up and left.
if the robot go up, it will print 'u'
if the robot go left, it will print 'l'

6, (bouns)user can random select the start point and end point

#run environment
python version 2.7

#How to run it.

just in command line:
```
python setmain.py
```
#test
this code use unittest to test some the example inputs.
The test all case command:

```
python test.py
```
The caseA is the example case.
The simpleA is more complex which is allow up and left from random start point to the end random point.


#algorithm:

Currently, I apply the Astarsearch algorithm for the pseudocode of this algoeithm is:

```
function A*(start, goal)
    // The set of nodes already evaluated.
    closedSet := {}
    // The set of currently discovered nodes still to be evaluated.
    // Initially, only the start node is known.
    openSet := {start}
    // For each node, which node it can most efficient be reach from.
    // If a node can be reached from many nodes, cameFrom will eventually contain the
    // most efficient previous step.
    cameFrom := the empty map

    // For each node, the cost of getting from the start node to that node.
    gScore := map with default value of Infinity
    // The cost of going from start to start is zero.
    gScore[start] := 0
    // For each node, the total cost of getting from the start node to the goal
    // by passing by that node. That value is partly known, partly heuristic.
    fScore := map with default value of Infinity
    // For the first node, that value is completely heuristic.
    fScore[start] := heuristic_cost_estimate(start, goal)

    while openSet is not empty
        current := the node in openSet having the lowest fScore[] value
        if current = goal
            return reconstruct_path(cameFrom, goal)

        openSet.Remove(current)
        closedSet.Add(current)
        for each neighbor of current
            if neighbor in closedSet
                continue		// Ignore the neighbor which is already evaluated.
            // The distance from start to goal passing through current and the neighbor.
            tentative_gScore := gScore[current] + dist_between(current, neighbor)
            if neighbor not in openSet	// Discover a new node
                openSet.Add(neighbor)
            else if tentative_gScore >= gScore[neighbor]
                continue		// This is not a better path.

            // This path is the best until now. Record it!
            cameFrom[neighbor] := current
            gScore[neighbor] := tentative_gScore
            fScore[neighbor] := gScore[neighbor] + heuristic_cost_estimate(neighbor, goal)

    return failure

function reconstruct_path(cameFrom, current)
    total_path := [current]
    while current in cameFrom.Keys:
        current := cameFrom[current]
        total_path.append(current)
    return total_path
```

In summary, the next ceil will put into the priority queue as the candidates to expend to the next step. The best weight cadidate will get to highest prority to expend the path.
the order is depending on the function
```
    f(n) = g(n) + h(n)
```

g(n) is the cost of the path from the start node to n, and

h(n) is a heuristic that estimates the cost of the cheapest path from n to the goal.


The use heapq library to fulfill the priority queue.

##about heuristic function:

```
heuristic(startx, starty, endx,endy)
```
Actually, Dijksta's algoeithm is the special A* search Algorithm case, which h(n)=0

The algorithm speed is determined by the heuristic function, that is why I use A* algorithm to solve this problem.
If h(n) is sometimes greater than the cost of moving from n to the goal, then A* is not guaranteed to find a shortest path, but it can run faster.

For this case since the question is only want to make the best way do not limited the time consumption. I use very low h(n), which is only cost 1 per ceil, it goes. It may useless for this case, but I put the h(n) function here to control the speed of your search if you like rewrtie it.

## about openmap and the only right and down solution.
the closemap record the ceils the robot already visit

the openmap record the ceils the robot need to visit

If The only right and down and there is no repeat visit, just use the Greedy Best-First-Search Algorithm would be OK.
