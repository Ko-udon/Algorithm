import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;

        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] ints : edge) {
            graph.get(ints[0]).add(ints[1]);
            graph.get(ints[1]).add(ints[0]);
        }

        boolean[] visited = new boolean[n+1];
        visited[1] = true;

        Queue<Integer> bfs = new LinkedList<>();
        bfs.add(1);

        int[] distance = new int[n+1];

        while (!bfs.isEmpty()) {
            int nowNode = bfs.poll();
            ArrayList<Integer> node = graph.get(nowNode);
            for (int i = 0; i < node.size(); i++) {
                if (!visited[node.get(i)]) {
                    visited[node.get(i)] = true;
                    bfs.add(node.get(i));
                    distance[node.get(i)] = distance[nowNode] + 1;
                }
            }
        }

        Arrays.sort(distance);
        int max = distance[n];

        for(int i = 0; i<distance.length; i++){
            if(distance[i] == max){
                answer++;
            }
        }

        return answer;
    }
}