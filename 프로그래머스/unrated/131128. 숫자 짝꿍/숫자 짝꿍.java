import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Solution {
    static public String solution(String x, String y) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        int[] xCount={0,0,0,0,0,0,0,0,0,0};
        int[] yCount={0,0,0,0,0,0,0,0,0,0};
        
        for(int i=0;i<x.length();i++){
            xCount[x.charAt(i)-'0']++;    
        }
        
        for(int i=0;i<y.length();i++){
            yCount[y.charAt(i)-'0']++;    
        }
        
        for(int i=9;i>-1;i--){
            if(xCount[i]>yCount[i]){
                sb.append(String.valueOf(i).repeat(yCount[i]));
            }
            else if(xCount[i]==yCount[i]){
                sb.append(String.valueOf(i).repeat(yCount[i]));
            }
            else{
                sb.append(String.valueOf(i).repeat(xCount[i]));
            }
        }
        if(sb.length() == 0){  //같은게 없다면
            return "-1";
        } 
        else if (sb.charAt(0) == '0') {  //
            return "0";
        }
        return sb.toString();
    }
}