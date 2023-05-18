import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        int answer = enemy.length;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        int now = n;
        int skill = k;
        
        for(int i = 0; i<enemy.length; i++){
            now -= enemy[i];
            pq.add(enemy[i]);
            
            if(now < 0) {
                if(skill > 0 && (!pq.isEmpty())){ //무적권 사용횟수가 남았고, pq에 값이 있다면
                    
                    now += pq.poll();
                    skill--;
                    
                } else{
                    answer = i;
                    break;
                    
                }
                
                
                
            }
            
            
            
        }
        
        return answer;
    }
}