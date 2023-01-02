import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
    PriorityQueue<Integer> pq=new PriorityQueue<>();
    for(int i:scoville){
      pq.add(i);
    }
    while(pq.peek()<K){
      if(pq.size()==1){
        return -1;
      }
      int n=pq.poll();
      int t=pq.poll();
      pq.add(n+(t*2));
      answer++;
    }
    return answer;

    }
}