#Assumptions&reasons:

1, the input number is considered as hexadecimal numbers: for example the 46B will regards the number 1131 in decimal.

2, the cost of from one cell of array to its neighbor is: the number of this cell cost add
the that number of its neighbor and then divided 2.
which is represent the cost function:

```
def cost(self, x1,y1,x2,y2):
    return (self.map[y1][x1]+self.map[y2][x2])/2
```
(it is reasonable to consider the distance caculation by arithmetic mean)

3, the minify number of cost represent the cell is 1(no zero cost), and the cost should be integer number. (I think in the real world the travel distance must be positive cost.)

4, the input numbers must be as array.

5, (bouns)the algorithm will consider allowing the robot up and left.
if the robot go up, it will print 'u'
if the robot go left, it will print 'l'

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

I use prority queue to fulfill this algorithm.
The use heapq library to fulfill the function.

##about heuristic function:
```
    f(n) = g(n) + h(n)
```
g(n) is the cost of the path from the start node to n, and

h(n) is a heuristic that estimates the cost of the cheapest path from n to the goal.

Actually, Dijksta's algoeithm is the special A* search Algorithm case, which h(n)=0
