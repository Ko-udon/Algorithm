class Solution {
    public int solution(String s) {
        int answer = 0;
        
        int x = 0;
        int y = 0;
        int i = 0;
        char c = ' ';
        while(i < s.length()){
            
            if(c == ' '){
                c = s.charAt(i);
            }
            
            if(c == s.charAt(i)){
                x++;
            }else{
                y++;
            }
            
            if(i == s.length() - 1){
                answer++;
                break;
            }
            
            if(x == y){
                answer++;
                x = 0;
                y = 0;
                c = ' ';
            }
            
            i++;
            
        }
        
        return answer;
    }
}