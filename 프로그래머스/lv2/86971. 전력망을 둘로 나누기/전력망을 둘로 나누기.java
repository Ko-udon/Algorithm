import java.util.LinkedList;
import java.util.Queue;


class Solution {
    static int arr[][];
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        arr = new int[n+1][n+1];

        //선 연결
        for(int i=0;i<wires.length;i++){
            arr[wires[i][0]][wires[i][1]] = 1;
            arr[wires[i][1]][wires[i][0]] = 1;
        }

        /*System.out.println("선 연결");
        for(int i=0;i<arr.length;i++){
            for (int j=0;j<arr[i].length;j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }*/

        //선을 하나씩 끊으며 순회하기
        int a,b;
        for(int i=0;i<wires.length;i++){
            a=wires[i][0];
            b=wires[i][1];

            //선 끊기
            arr[a][b]=0;
            arr[b][a]=0;

            //bfs
            answer= Math.min(answer,bfs(n,a));


            //선 복구
            arr[a][b]=1;
            arr[b][a]=1;
        }


        return answer;
    }
     public int bfs(int n, int start){
        int[] visit= new int[n+1];
        int cnt=1;

        Queue<Integer> queue= new LinkedList<>();
        queue.offer(start);

        while(!queue.isEmpty()){
            int point= queue.poll();
            visit[point]= 1;

            for(int i=1; i<=n; i++){ //point와 연결된 애들 중에 방문한적 없는 노드 전부 큐에 넣기
                if(visit[i]==1) continue;

                //연결이 되있는 간선이라면
                if(arr[point][i]==1) {
                    queue.offer(i);
                    cnt++;
                }
            }
        }
        return (int)Math.abs(n-2*cnt); //cnt-(n-cnt);
    }//bfs
}