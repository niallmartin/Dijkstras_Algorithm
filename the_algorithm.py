import sys
import pandas as pd

input_file = sys.argv[1]
data = pd.read_csv(input_file)

Length = data.ix[37528:(37527+39956), ['37527']]
dfList = Length['37527'].tolist()


# This function is used to split the values into a dictionart with format { starting_node {end_node, weight}}

def values_to_dict(list):
    returned_dict = {}
    value = []
    for i in list:
        val = i.split()
        if int(val[0]) not in returned_dict:
            returned_dict[int(val[0])] = {}
            returned_dict[int(val[0])][int(val[1])] = int(val[2])
        else:
            returned_dict[int(val[0])][int(val[1])] = int(val[2])
    return returned_dict



# # Code - For Dijkstra's algorithm

import heapq

def shortestPath_test(input_list, start, end):
    queue = [(0, start, [])]
    seen = set()
    
    while True: # No vertices left to explore when False
        
        try:
            # Note: heapq provides an implementation of the heap queue algorithm,
            # also known as the priority queue algorithm.
            distance, location, path = heapq.heappop(queue) # This returns the smallest item from the heap, maintaining the heap invariant
            #print 'POP:', distance, location, path # Uncomment to see what values were popped from the heap
        except IndexError:
            print "No Path To Final Location"
            return distance, path
        
        if location not in seen:
            path = path + [location]
            seen.add(location)
            
            if location == end:
                return distance, path
            
            elif location not in List:
                continue
            
            else:
                for (next_location, next_distance) in input_list[location].items():
                    heapq.heappush(queue, (distance + next_distance, next_location, path))
                    #print "PUSH:", next_location, next_distance # Uncomment to see what values were pushed to the heap


# Call The Function Here


List = values_to_dict(dfList)
Start = int(sys.argv[2])
End = int(sys.argv[3])

if Start in List:
    Distance, Path = shortestPath_test(List,Start,End)
    print "The shortest distance between %s and %s is %s" % (Start, End, Distance)
else:
    print "At least one of the nodes is not in the map"

