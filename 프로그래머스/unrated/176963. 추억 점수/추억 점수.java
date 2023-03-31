import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        
        int num = 0;
        for(String[] photos : photo){
            int result = 0;
            for(String s : photos){
                for(String names : name){
                    if(names.equals(s)){
                        result+=yearning[Arrays.asList(name).indexOf(names)];
                        break;
                    }
                }
            }
            
            answer[num] = result;
            num++;
        }
        return answer;
    }
}