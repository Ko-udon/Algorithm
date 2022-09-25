import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
               
        if(arr.length<=1){
            int[] ans={-1};
            return ans;
        }
        else{
            
          
            int min=arr[0];
            for(int i=0;i<arr.length;i++){
                if(min>arr[i]){
                    min=arr[i];
                }
            }
            int[] answer = new int[arr.length-1];
            ArrayList<Integer> list=new ArrayList<Integer>();
            for(int i:arr){
                list.add(i);
            }
            
            list.remove(new Integer(min));
            for(int i=0;i<list.size();i++){
                
                answer[i]=list.get(i);
            }
            
            
        
            return answer;
        }
        
    }
}