import java.util.*;
import java.util.ArrayList;


public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> al=new ArrayList<Integer>();
    
        for(int i=0;i<arr.length-1;i++){
            if(arr[i]!=arr[i+1]){
                al.add(arr[i]);
            }
        }
        al.add(arr[arr.length-1]);
        int[] answer = new int[al.size()];
        for(int i=0;i<al.size();i++){
            answer[i]=al.get(i);
        }

        return answer;
    }
}