# Dijkstras Algorithm
Here I implement a shortest path algorithm to find the minimum distance between nodes in a graph.

## Code Requirements:

- The code was developed using python 2.7
- The following packages are required:
    - pandas to split the data.
    - heapq to implement a priority queue for Dijkstra’s algorithm.

## Notes:

1. As mentioned, I chose to a shortest path algorithm to find the values. More specifically, I chose to use Dijkstra’s algorithm as “This is asymptotically the fastest known single-source shortest-path algorithm for arbitrary directed graphs with unbounded non-negative weights” [1]. Based on this statement, the algorithm can be applied to more problems in the future.
2. I chose to parse the values in a dictionary using the function values_to_dict with the format {“start_node“{“end_node“,“distance“}}. This ensured that fast access to data was available, as dictionaries are based on hash tables. 

## Running Code:

The code is run using the following command, which contains three arguments:
./run.sh {data_name} {starting_node} {end_node}

For example:

 ./run.sh map_data.dat 316319897 316319936

