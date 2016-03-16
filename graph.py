from heapq import heappop, heappush

class Graph:
    def __init__(self, set_dimensions, set_rules, set_start):
        self.width = set_dimensions[0]
        self.height = set_dimensions[1]
        self.rules = set_rules
        self.start = set_start

    def getAdjacent(self, location, direction):
        """
        Finds the adjacent square in the graph through ugly if-else logic and possibly recursion
        if the adjacent square is a teleporter
        Args:
            location  - x, y coordinates that map to the 2D array that represents the graph
            direction - an int that represents the direction the snake is currently traveling
                        0 -> right
                        2 -> down
                        4 -> left
                        6 -> up
        Returns:
            If the adjacent point is pathable, return it, otherwise return None.
        """

        # direction is right
        if direction == 0:
            if location[0] + 1 >= self.width:
                return None
            elif self.rules[location[0] + 1][location[1]] == 'Wall':
                return None
            elif self.rules[location[0] + 1][location[1]] == 'None' or self.rules[location[0] + 1][location[1]] == 'Open' or self.rules[location[0] + 1][location[1]] == 'Start':
                return [location[0] + 1, location[1]]
            else:
                teleporter = self.rules[location[0] + 1][location[1]] # save the tp #
                for x, column in enumerate(self.rules): # iterate through the self.rules to find the tp
                    for y, value in enumerate(column):
                        if value == teleporter and (x != location[0] + 1 or y != location[1]):
                            return self.getAdjacent([x, y], 0) # retry the check at the new position
                return None # there is no matching teleporter
        # direction is down
        elif direction == 2:
            if location[1] + 1 >= self.height:
                return None
            elif self.rules[location[0]][location[1] + 1] == 'Wall':
                return None
            elif self.rules[location[0]][location[1] + 1] == 'None' or self.rules[location[0]][location[1] + 1] == 'Open' or self.rules[location[0]][location[1] + 1] == 'Start':
                return [location[0], location[1] + 1]
            else:
                teleporter = self.rules[location[0]][location[1] + 1] # save the tp #
                for x, column in enumerate(self.rules): # iterate through the self.rules to find the tp
                    for y, value in enumerate(column):
                        if value == teleporter and (x != location[0] or y != location[1] + 1):
                            return self.getAdjacent([x, y], 2) # retry the check at the new position
                return None # there is no matching teleporter
         # direction is left
        elif direction == 4:
            if location[0] - 1 < 0:
                return None
            elif self.rules[location[0] - 1][location[1]] == 'Wall':
                return None
            elif self.rules[location[0] - 1][location[1]] == 'None' or self.rules[location[0] - 1][location[1]] == 'Open' or self.rules[location[0] - 1][location[1]] == 'Start':
                return [location[0] - 1, location[1]]
            else:
                teleporter = self.rules[location[0] - 1][location[1]] # save the tp #
                for x, column in enumerate(self.rules): # iterate through the self.rules to find the tp
                    for y, value in enumerate(column):
                        if value == teleporter and (x != location[0] - 1 or y != location[1]):
                            return self.getAdjacent([x, y], 4) # retry the check at the new position
                return None # there is no matching teleporter
        # direction is up
        else:
            if location[1] - 1 < 0:
                return None
            elif self.rules[location[0]][location[1] - 1] == 'Wall':
                return None
            elif self.rules[location[0]][location[1] - 1] == 'None' or self.rules[location[0]][location[1] - 1] == 'Open'  or self.rules[location[0]][location[1] - 1] == 'Start':
                return [location[0], location[1] - 1]
            else:
                teleporter = self.rules[location[0]][location[1] - 1] # save the tp #
                for x, column in enumerate(self.rules): # iterate through the self.rules to find the tp
                    for y, value in enumerate(column):
                        if value == teleporter and (x != location[0] or y != location[1] - 1):
                            return self.getAdjacent([x, y], 6) # retry the check at the new position
                return None # there is no matching teleporter

    def convertToDir(self, list):
        # Takes in a list of coordinates and returns a list of directions that links them
        #for i, coord in enumerate(list):
        return None


    def findPathsDFS(self):
        # Returns all valid paths through the defined graph
        # Returns:
        #    A list of paths in the form of a list of directions
    
        path = [self.start]
        stack = [(self.start, None)]
        path_list = []
        while stack:
            while stack[-1][1] == path[-1] or len(path) == 1:         # if the next position is adjacent to the head
                v = stack.pop()     # get the next snake position
                if len(path) != 1 or v[0] != self.start:
                    path.append(v[0])      # append it to the path
                i = 6
                while i >= 0:       # get and the next three adjacent positions
                    adj = [self.getAdjacent(v[0], i), None]
                    if adj[0] and (adj[0] not in path or (adj[0] == self.start and len(path) > 1)):
                        adj[1] = v[0]          # store parent
                        stack.append(adj)      # if not walls or OOB add them to the stack
                    elif adj[0] == self.start:
                        print('shrek')
                    i -= 2
                if len(stack) == 0:
                    break
            #print(path[-1])
            if path[-1] == self.start:
                path_list.append(path)                                      # if not and the head is the start save the list
            if path:
                path.pop()                                                      # pop off the head of the path
        #for p in path_list:
            #p = convertToDir(p)
        return path_list


# Test graph
#   None    TP 1    None    Start
#   Wall    None    None    None
#   None    Open    None    None
#   None    None    TP 1    None
#   None    None    None    None

sample_rules = [
    [ 'None', 'Wall', 'None', 'None', 'None'],
    [      1, 'None', 'Open', 'None', 'None'],
    [ 'None', 'None', 'None',      1, 'None'],
    ['Start', 'None', 'None', 'None', 'None']
]

sample_graph = Graph([4, 5], sample_rules, [3, 0])

#adjacent = sample_graph.getAdjacent([1,4],6)
#print(adjacent)

#paths = sample_graph.findPathsDFS()
#print(paths)