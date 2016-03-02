from graph import Graph

# Test graph
#   None    TP 1    None    Start
#   Wall    None    None    None
#   None    Open    None    None
#   None    None    TP 1    None
#   None    None    None    None

sample_rules = [
    ['None', 1, 'None', 'None'],
    ['Wall', 'None', 'None', 'None'],
    ['None', 'Open', 'None', 'None'],
    ['None', 'None', 1, 'None'],
    ['None', 'None', 'None', 'None']
]

sample_graph = Graph([4, 5], sample_rules, [0, 3])

sample_correct_path1 = [4, 4, 6, 4, 2, 2, 0, 0, 0, 6, 6, 6, 6]
sample_incorrect_path1 = [4, 2, 0, 6]
sample_incorrect_path2 = [4, 2, 4, 2, 0, 0, 6, 6]


# Checks if given path adheres to all rules in given graph
def checkCorrectness(graph, path):
    return None


# Exports graph to image that is usable by game
def exportToPNG(graph, path, name):
    return None
