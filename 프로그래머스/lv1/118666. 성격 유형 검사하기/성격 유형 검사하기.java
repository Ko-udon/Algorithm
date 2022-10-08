import java.util.Set;
import java.util.Map;
import java.util.HashMap;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        Map<String, Integer> map = new HashMap<>();
        map.put("R",0);
        map.put("T",0);
        map.put("C",0);
        map.put("F",0);
        map.put("J",0);
        map.put("M",0);
        map.put("A",0);
        map.put("N",0);
        
        for(int i=0;i<survey.length;i++){
            String c1=survey[i].substring(0,1);
            String c2=survey[i].substring(1);
            int n=choices[i];
            switch(n){
                case 1:
                    map.put(c1,map.get(c1)+3);
                    break;
                case 2:
                    map.put(c1,map.get(c1)+2);
                    break;
                case 3:
                    map.put(c1,map.get(c1)+1);
                    break;
                case 4:
                    break;
                case 5:
                    map.put(c2,map.get(c2)+1);
                    break;
                case 6:
                    map.put(c2,map.get(c2)+2);
                    break;
                case 7:
                    map.put(c2,map.get(c2)+3);
                    break;
                    
            }
        }
        
        if(map.get("R")>map.get("T")){
            answer+="R";
        }
        else if(map.get("R")<map.get("T")){
            answer+="T";
        }
        else{
            answer+="R";
        }
        
        if(map.get("C")>map.get("F")){
            answer+="C";
        }
        else if(map.get("C")<map.get("F")){
            answer+="F";
        }
        else{
            answer+="C";
        }
        
        if(map.get("J")>map.get("M")){
            answer+="J";
        }
        else if(map.get("J")<map.get("M")){
            answer+="M";
        }
        else{
            answer+="J";
        }
        
        if(map.get("A")>map.get("N")){
            answer+="A";
        }
        else if(map.get("A")<map.get("N")){
            answer+="N";
        }
        else{
            answer+="A";
        }
        
        
        return answer;
    }
}