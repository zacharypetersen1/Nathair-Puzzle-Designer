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
            if rules[location[0] + 1, location[1]] == 'Wall' or location[0] + 1 > width:
                return None
            elif rules[location[0] + 1, location[1]] == 'None' or rules[location[0] + 1, location[1]] == 'Open':
                return [location[0] + 1, location[1]]
            else:
                teleporter = rules[location[0] + 1, location[1]] # save the tp #
                for x, column in enumerate(rules): # iterate through the rules to find the tp
                    for y, value in enumerate(column):
                        if value == teleporter and (x != location[0] or y != location[1]):
                            return getAdjacent([x, y], 0) # retry the check at the new position
                        else: # there is no matching teleporter
                            return None
        # direction is down
        elif direction == 2:    
            if rules[location[0], location[1] + 1] == 'Wall':
                return None
            elif rules[location[0], location[1] + 1] == 'None' or rules[location[0], location[1] + 1] == 'Open':
                return [location[0], location[1] + 1]
            else:
                teleporter = rules[location[0], location[1] + 1] # save the tp #
                for x, column in enumerate(rules): # iterate through the rules to find the tp
                    for y, value in enumerate(column):
                        if value == teleporter and (x != location[0] or y != location[1]):
                            return getAdjacent([x, y], 2) # retry the check at the new position
                        else: # there is no matching teleporter
                            return None
         # direction is left
        elif direction == 4:   
            if rules[location[0] - 1, location[1]] == 'Wall':
                return None
            elif rules[location[0] - 1, location[1]] == 'None' or rules[location[0] - 1, location[1]] == 'Open':
                return [location[0] - 1, location[1]]
            else:
                teleporter = rules[location[0] - 1, location[1]] # save the tp #
                for x, column in enumerate(rules): # iterate through the rules to find the tp
                    for y, value in enumerate(column):
                        if value == teleporter and (x != location[0] or y != location[1]):
                            return getAdjacent([x, y], 4) # retry the check at the new position
                        else: # there is no matching teleporter
                            return None
        # direction is up
        else:                       
            if rules[location[0], location[1] - 1] == 'Wall':
                return None
            elif rules[location[0], location[1] - 1] == 'None' or rules[location[0], location[1] - 1] == 'Open':
                return [location[0], location[1] - 1]
            else:
                teleporter = rules[location[0], location[1] - 1] # save the tp #
                for x, column in enumerate(rules): # iterate through the rules to find the tp
                    for y, value in enumerate(column):
                        if value == teleporter and (x != location[0] or y != location[1]):
                            return getAdjacent([x, y], 6) # retry the check at the new position
                        else: # there is no matching teleporter
                            return None

    def convertToDir(self, list):
        # Takes in a list of coordinates and returns a list of directions that links them
        return None


    def findPathsDFS(self):
        # Returns all valid paths through the defined graph
        # Returns:
        #    A list of paths in the form of a list of coordinates
    
        path = []
        stack = [(0, start)]
        path_list = [(0, start)]
        parent = {}
        while queue:
            while parent[stack[len(stack) - 1]] == path[len(path) - 1]:     # if the next position is adjacent to the head 
                v = stack.pop()     # get the next snake position
                path.append(v)      # append it to the path
                i = 6
                while i <= 0:       # get and the next three adjacent positions
                    adj = getAdjacent(v, i)
                    if (adj and adj not in path) or adj == start:
                        stack.append(adj)   # if not walls or OOB add them to the stack
                        parent[adj] = v     # give adjacent values parents in the dict
                    i -= 2
            if(path[len(path) - 1] == start)
                path_list.append(path)                                      # if not and the head is the start save the list
            path.pop()                                                      # pop off the head of the path
        for p in path_list:
            p = convertToDir(p)
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