from sys import stdin


class Graph:
    def __init__(self) -> None:
        self.nodes = {}

    def add_adjacent(self, content1: str, content2: str) -> None:
        if content1 not in self.nodes:
            self.nodes[content1] = []
        if content2 not in self.nodes:
            self.nodes[content2] = []
        self.nodes[content1].append(content2)
        self.nodes[content2].append(content1)

    def find_three(self) -> int:
        three_computers = set()
        for node in self.nodes.keys():
            if node[0] != "t":
                continue
            for adjacent in self.nodes[node]:
                for neighbor in self.nodes[adjacent]:
                    if node in self.nodes[neighbor]:
                        three_computers.add(tuple(sorted([node, adjacent, neighbor])))
        return len(three_computers)

line: str = stdin.readline().strip()
graph = Graph()
while line:
    content1, content2 = line.split("-")
    graph.add_adjacent(content1, content2)
    line = stdin.readline().strip()
print(graph.find_three())
