from graph import Graph

# Test graph
#   None    TP 1    None    Start
#   Wall    None    None    None
#   None    Open    None    None
#   None    None    TP 1    None
#   None    None    None    None
"""
sample_rules = [
    ['None', 'Wall', 'None', 'None', 'None'],
    [1, 'None', 'Open', 'None', 'None'],
    ['None', 'None', 'None', 1, 'None'],
    ['Start', 'None', 'None', 'None', 'None']
]
"""

sample_graph = Graph([4, 5], sample_rules, [3, 0])

sample_correct_path1 = [4, 4, 6, 4, 2, 2, 0, 0, 0, 6, 6, 6, 6]
sample_incorrect_path1 = [4, 2, 0, 6]
sample_incorrect_path2 = [4, 2, 4, 2, 0, 0, 6, 6]

#returns array of locations of open spaces (2-tuple) 
def get_open_spaces(graph):
    open_spaces = []
    for x in range(0, graph.width):
        for y in range(0, graph.height):
            #if graph.rules[x][y] is open, push onto list
            element = graph.rules[x][y]
            if type (element) is str:
                if element == 'Open':
                    print("Found an open element at:", x, y)
                    open_spaces.append([x,y])
    return open_spaces
    

# Checks if given path adheres to all rules in given graph
def checkCorrectness(graph, path):
    open_spaces = get_open_spaces(graph)
    print ("open_spaces:", open_spaces)
    adjacent = graph.start
    for direction in path:
        print ("adjacent:", adjacent)
        adjacent = graph.getAdjacent(adjacent, direction)
        if (adjacent == None):
            print("invalid path:", path)
            return False
        if adjacent in open_spaces:
            open_spaces.remove(adjacent)
            #remove adjacent from open_spaces
    print ("open_spaces:", open_spaces)
    return open_spaces == []


# Exports graph to image that is usable by game
def exportToPNG(graph, path, name):
    return None

    
if __name__ == "__main__":
    print ("correct path:", checkCorrectness(sample_graph, sample_correct_path1))
    print ("incorrect path 1:", checkCorrectness(sample_graph, sample_incorrect_path1))
    print ("incorrect path 2:", checkCorrectness(sample_graph, sample_incorrect_path2))