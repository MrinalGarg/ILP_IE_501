# Longest Route Finder
This is a project for finding a closed circuit(Not necessarily Hamiltonian) in a graph with weighted edges which has the maximum sum of weights of its edges. The code provided is written using the **mip** Python library and **CBC** solver for Mixed integer programming.
## Input
The data provided into the code in the format of a 2-D Matrix of size $n$ where n represents the total number of nodes and each entry in the matrix contains weight of the edge betweeen those two nodes. If somewhere an edge is not present, weight is entered as a large negative value with modulus greater than the sum of all valid weights. 
## Output
Output contains all the information that standard CBC solver prints. At the end is the maximum sum of weights achieven on th optimized cycle followed by a line-wise value of the variable 2-D matrix, i.e. '1' or '0' depending on weather a particular directed edge is present in the directed cycle or not.
## Remarks
The file **Data.py** contains the input matrix (of size 36 ) for the map on IIT Bombay. It is to be noted that the no. of constraints are of exponential order and hence the time taken to output the result with increasing number of nodes increases sharply. The code file by default contains a classic example matrix of size 6 where the graphn is essentially two triangles connected by a single edge between one of their vertices. The code file outputs the cycle as the triangle with greater sum which is what is expected of it.
