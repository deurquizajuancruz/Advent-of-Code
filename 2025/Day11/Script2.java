import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Script2 {

    private static class Node {
        private String content;
        private List<Node> adjacent;

        public Node(String content) {
            this.content = content;
            this.adjacent = new ArrayList<>();
        }

        public String getContent() {
            return this.content;
        }

        public void addAdjacent(Node node) {
            this.adjacent.add(node);
        }
    }

    private static class Graph {
        private Map<String, Long> memoCache;
        private List<Node> nodes;

        public Graph() {
            this.nodes = new ArrayList<Node>();
            this.memoCache = new HashMap<>();
        }

        public void addNode(Node node) {
            this.nodes.add(node);
        }

        public Node inGraph(String contentNode) {
            for (Node node : this.nodes) {
                if (node.getContent().equals(contentNode)) {
                    return node;
                }
            }
            return null;
        }

        public long countPaths(String startNodeName) {
            Node start = this.inGraph(startNodeName);
            if (start == null)
                return 0;
            return dfs(start, false, false);
        }

        private long dfs(Node current, boolean hasDac, boolean hasFft) {
            boolean newDac = hasDac || current.getContent().equals("dac");
            boolean newFft = hasFft || current.getContent().equals("fft");

            String stateKey = current.getContent() + "|" + newDac + "|" + newFft;

            if (memoCache.containsKey(stateKey)) {
                return memoCache.get(stateKey);
            }

            if (current.getContent().equals("out")) {
                return (newDac && newFft) ? 1 : 0;
            }

            long paths = 0;
            for (Node adj : current.adjacent) {
                paths += dfs(adj, newDac, newFft);
            }

            memoCache.put(stateKey, paths);
            return paths;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Graph myGraph = new Graph();

        while (scanner.hasNextLine()) {
            String line = scanner.nextLine().trim();

            String[] divided = line.split(":");

            String originName = divided[0].trim();
            Node origin = myGraph.inGraph(originName);
            if (origin == null) {
                origin = new Node(divided[0]);
                myGraph.addNode(origin);
            }

            String[] adjacents = divided[1].trim().split(" ");
            for (String adj : adjacents) {
                Node adjacentNode = myGraph.inGraph(adj);
                if (adjacentNode == null) {
                    adjacentNode = new Node(adj);
                    myGraph.addNode(adjacentNode);
                }
                origin.addAdjacent(adjacentNode);
            }
        }
        scanner.close();

        long result = myGraph.countPaths("svr");
        System.out.println(result);
    }
}