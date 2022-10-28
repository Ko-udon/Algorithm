import java.util.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        System.out.println(0);
        Arrays.sort(citations);
        for(int i=0;i<citations.length;i++){
            int h=citations.length-i;
            
            if(citations[i]>=h){
                answer=h;
                break;
            }
            
        }
          
        return answer;
    }
}