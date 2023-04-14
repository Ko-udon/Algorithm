import java.util.*;

class Solution {
    
    
    public int solution(String s) {
        int min = s.length();
        
        for(int i = 1; i < s.length(); i++){
          
            min = Math.min(min, check(s,i));
            
            
        }
      
        return min;
    }
    
    public int check(String s, int size){
        int len = 0;
        String cutS = s.length() % size == 0 ?"":  
            s.substring(s.length() - (s.length() % size) , s.length());
        
        StringBuilder sb = new StringBuilder();
        int count = 1;
        String st = "";
        
        for(int i = 0; i<=s.length() - size; i+=size){
            String tmp = s.substring(i, size+i);
            
            if(st.equals(tmp)){
                count++;
            }else{
                if(count == 1 || count == 0){
                    sb.append(st);
                } else{
                    sb.append((count+st));    
                }
                st = tmp;
                count = 1;
                
            }
               
        }
        
        if(count == 1 || count == 0){
            sb.append(st);
        } else{
            sb.append((count+st));    
        }
        
        sb.append(cutS);

        return sb.length();
    }
}