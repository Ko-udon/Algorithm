import java.util.HashMap;
import java.util.Map;

class Solution {
    public String[] solution(String[] record) {
        Map<String,String> map=new HashMap<>();
        int printSize=0;
        for(int i=0;i<record.length;i++){
            String[] str=record[i].split(" ");
            if(str[0].equals("Enter")|str[0].equals("Change")){
                map.put(str[1],str[2]);
            }
            if(str[0].equals("Enter")|str[0].equals("Leave")){
                printSize++;
            }
        }


        //System.out.println(map);
        //System.out.println(printSize);

        String[] answer=new String[printSize];
        int msgTmp=0;
        for(int i=0;i<record.length;i++){
            String[] str=record[i].split(" ");
            switch (str[0]){
                case "Enter":
                    answer[msgTmp]=map.get(str[1])+"님이 들어왔습니다.";
                    msgTmp++;
                    break;
                case "Leave":
                    answer[msgTmp]=map.get(str[1])+"님이 나갔습니다.";
                    msgTmp++;
                    break;
                default:
                    break;
            }
        }

    
        return answer;
    }
}