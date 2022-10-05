import java.util.ArrayList;
class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        int[] arr =new int[3];
        int idx = 0;
        String tmp="";
        for(int i=0;i<dartResult.length();i++){
            char c=dartResult.charAt(i);
            char ch=' ';
            switch(c){
                case 'S':   
                    arr[idx]=Integer.parseInt(tmp);
                    idx++;
                    tmp="";
                    break;
                case 'D':   
                    arr[idx]=(int)Math.pow(Integer.parseInt(tmp),2);
                    idx++;
                    tmp="";
                    break;
                case 'T':
                    arr[idx]=(int)Math.pow(Integer.parseInt(tmp),3);
                    idx++;
                    tmp="";
                    break;
                    
                    
                case '*':
                    arr[idx-1]*=2;
                    if(idx >1) arr[idx-2]*=2;
                    break;
                    
                case '#':
                    arr[idx-1]*=-1;
                    break;
                    
                default:
                    tmp+=String.valueOf(dartResult.charAt(i));
                    break;
                    
            }
        }
        for(int i:arr){
            System.out.println(i);
            answer+=i;
        }
        return answer;
    }
}