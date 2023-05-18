import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 1;
        
        Arrays.sort(targets, (a,b) -> {
            if(a[1] == b[1]){
                return a[0] - b[0];
            }
            return a[1] - b[1];
        });
        
        int endPoint =targets[0][1];
        
        for(int[] t : targets){
            if(t[0]>=endPoint){
                endPoint = t[1];
                answer++;
            }
            
            
            
        }
        return answer;
    }
}