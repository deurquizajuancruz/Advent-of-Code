import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Script {

    private static class Node {
        private String content;
        private List<Node> adjacent;
        private boolean visited;

        public Node(String content) {
            this.content = content;
            this.adjacent = new ArrayList<Node>();
            this.visited = false;
        }

        public void addAdjacent(Node node) {
            this.adjacent.add(node);
        }

        public String getContent() {
            return this.content;
        }

        public void markVisited() {
            this.visited = true;
        }

        public void unmarkVisited() {
            this.visited = false;
        }

        public boolean isVisited() {
            return this.visited;
        }

        public int tour() {
            this.markVisited();
            int paths = 0;
            if (this.getContent().equals("out")) {
                paths = 1;
            } else if (this.adjacent.size() > 0) {
                for (Node adj : this.adjacent) {
                    if (!adj.isVisited()) {
                        paths += adj.tour();
                    }
                }
            }
            this.unmarkVisited();
            return paths;
        }
    }

    private static class Graph {
        List<Node> nodes;

        public Graph() {
            this.nodes = new ArrayList<Node>();
        }

        public Node inGraph(String contentNode) {
            for (Node node : this.nodes) {
                if (node.getContent().equals(contentNode)) {
                    return node;
                }
            }
            return null;
        }

        public void addNode(Node node) {
            this.nodes.add(node);
        }

    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Graph myGraph = new Graph();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            String[] divided = line.split(":");
            Node origin = myGraph.inGraph(divided[0]);
            if (origin == null) {
                origin = new Node(divided[0]);
                myGraph.addNode(origin);
            }
            String[] adjacentes = divided[1].trim().split(" ");
            for (String adj : adjacentes) {
                Node adjacentNode = myGraph.inGraph(adj);
                if (adjacentNode == null) {
                    adjacentNode = new Node(adj);
                    myGraph.addNode(adjacentNode);
                }
                origin.addAdjacent(adjacentNode);
            }
        }
        scanner.close();

        Node you = myGraph.inGraph("you");
        int paths = you.tour();
        System.out.println(paths);
    }
}