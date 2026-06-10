class Node:

    def __init__(self, name, action):
        self.name = name
        self.action = action

    def execute(self, state):
        return self.action(state)
class Graph:

    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def add_edge(self, source, destination):
        self.edges[source] = destination

    def get_next(self, current):
        return self.edges.get(current)    
class Runtime:

    def __init__(self, graph):
        self.graph = graph

    def run(self, start_node, state):

        current = start_node

        while current != "END":

            node = self.graph.nodes[current]

            state = node.execute(state)

            current = self.graph.get_next(current)

        return state 
       
def collect_data(state):

    print("CollectData node executing")

    state["data"] = "AI information"

    return state   
 
def analyze_data(state):

    print("AnalyzeData node executing")

    state["analysis"] = (
        f"Analysis of {state['data']}"
    )

    return state

graph = Graph()

graph.add_node(
    Node(
        "CollectData",
        collect_data
    )
)

graph.add_node(
    Node(
        "AnalyzeData",
        analyze_data
    )
)

graph.add_edge(
    "CollectData",
    "AnalyzeData"
)

graph.add_edge(
    "AnalyzeData",
    "END"
)
runtime = Runtime(graph)

result = runtime.run(
    "CollectData",
    {}
)

print("\nFinal State:")
print(result)