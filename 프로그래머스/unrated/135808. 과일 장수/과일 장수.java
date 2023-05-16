import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int i : score){
            pq.add(i);
        }
        
        while(pq.size() >= m){      
            
            for(int i = 0; i<m - 1; i++){
                pq.remove();
            }
            answer+=pq.poll() * m;     
        }
        return answer;
        
    }
    
    
}