class Solution {
    boolean solution(String s) {
       boolean answer = false;
        int countP=0;
        int countY=0;
        for(int i=0;i<s.length();i++){
            char c=s.charAt(i);
            if(c=='P'|c=='p'){
                countP++;
            }
            else if(c=='Y'|c=='y'){
                countY++;
            }

        }
        if(countP==countY){
            answer=true;
        }
        

        return answer;
    }
}