import java.util.*;

class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] pron = {"aya","ye","woo","ma"};
        
        for(int i = 0; i<babbling.length; i++){
            StringBuilder sb = new StringBuilder(babbling[i]);
            StringBuilder sb2 = new StringBuilder();
            int len = 0;
            int type = -1;
            while(len < sb.length() - 1){
                char c = sb.charAt(len);
                switch(c){
                    case 'a':
                        if(type != 0){
                            sb2.append("aya");
                            len+=3;   
                            type = 0;
                            break;
                        }
                        len = sb.length();
                        break;                       
                    case 'y':
                        if(type != 1){
                            sb2.append("ye");
                            len+=2;
                            type = 1;
                            break;    
                        }
                        len = sb.length();
                        break; 
                    case 'w':
                        if(type != 2){
                            sb2.append("woo");
                            len+=3;
                            type = 2;
                            break;
                        }
                        len = sb.length();
                        break; 
                    case 'm':
                        if(type != 3){
                            sb2.append("ma");
                            len+=2;
                            type = 3;
                            break;    
                        }
                        len = sb.length();
                        break;
                        
                    default:
                        len = sb.length();
                        break;

                }    
                
                
            }
            if(sb.toString().equals(sb2.toString())){
                answer++;
            }
            
            
            
        }
        return answer;
    }
}