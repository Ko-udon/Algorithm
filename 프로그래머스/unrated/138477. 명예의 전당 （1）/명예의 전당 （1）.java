import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        int[] result = new int[score.length];
        
        List<Integer> list = new ArrayList<>();
        int min = 0;
        
        for(int i = 0; i<score.length; i++){
            
            if(list.size() < k){
                list.add(score[i]);
            } 
            
            else{
                if(min < score[i]){
                    list.remove(Integer.valueOf(min));
                    list.add(score[i]);         
                }
                
            }
            
            min = Collections.min(list);
            
            result[i] = min;
            
        
        }
        return result;
    }
}