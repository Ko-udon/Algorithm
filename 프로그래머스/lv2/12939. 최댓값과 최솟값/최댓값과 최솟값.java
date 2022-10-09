import java.util.Arrays;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] num=s.split(" ");
        int[] numInt=new int[num.length];
        for(int i=0;i<num.length;i++){
            numInt[i]=Integer.parseInt(num[i]);
        }
        int min=numInt[0];
        int max=numInt[0];
        for(int i=1;i<numInt.length;i++){
            if(min>numInt[i]){
                min=numInt[i];
            }
            if(max<numInt[i]){
                max=numInt[i];
            }
            
        }
        
        
        return answer=min+" "+max;
    }
}