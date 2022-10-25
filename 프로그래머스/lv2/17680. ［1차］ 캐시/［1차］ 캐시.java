import java.util.*;
import java.util.Queue;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        if(cacheSize == 0) // 캐시크기가 0인 경우
            return cities.length * 5;
        Queue<String> queue=new LinkedList<>();
        int answer = 0;
        for(int i=0;i<cities.length;i++){
            String s=cities[i].toLowerCase();
            if(queue.remove(s)){
                answer+=1;
                queue.add(s);
            }
            else{
                answer+=5;
                if(queue.size()>=cacheSize){
                    queue.remove();
                }
                queue.add(s);
            }
        
        }
        
        
        
        return answer;
    }
}