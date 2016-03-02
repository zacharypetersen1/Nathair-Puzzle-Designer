

class Graph:
    def __init__(self, set_dimensions, set_rules, set_start):
        self.width = set_dimensions[0]
        self.height = set_dimensions[1]
        self.rules = set_rules
        self.start = set_start


    # Returns the location of the square in the desired direction
    #   or None if the move is not possible
    def getAdjacent(self, location, direction):
        return None


    # Returns all valid paths through this graph
    def findPathsDFS(self):
        return None



# Test graph
#   None    TP 1    None    Start
#   Wall    None    None    None
#   None    Open    None    None
#   None    None    TP 1    None
#   None    None    None    None

sample_rules = [
    ['None', 'Wall', 'None', 'None', 'None'],
    [1, 'None', 'Open', 'None', 'None'],
    ['None', 'None', 'None', 1, 'None'],
    ['Start', 'None', 'None', 'None', 'None']
]

sample_graph = Graph([4, 5], sample_rules, [3, 0])