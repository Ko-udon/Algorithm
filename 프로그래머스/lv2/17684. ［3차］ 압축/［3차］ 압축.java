import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int[] solution(String msg) {
        ArrayList<Integer> array = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>();
        
        char c='A';
        for(int i=1;i<27;i++){
            map.put(c+"",i);
            c+=1;
        }
        int endNum=27;
        
        boolean isEnd=false;
        for(int i=0;i<msg.length();i++){
            String word=msg.charAt(i)+"";
            while(map.containsKey(word)){
                i++;
                if(i==msg.length()){
                    isEnd=true;
                    break;
                }
                word+=msg.charAt(i);
            }
            if(isEnd==true){
                array.add(map.get(word));
                break;
            }
            array.add(map.get(word.substring(0,word.length()-1)));
            map.put(word,endNum++);
            i--;
                
            
        }
        
        int[] answer=new int[array.size()];
        for(int i = 0; i<array.size();i++){
            answer[i] = array.get(i);
        }
        return answer;
    }
}