class Solution {
    public String solution(int n) {
        String numbers[] = {"4","1","2"};
        String answer = "";
        
        while(n>0){
            int detect=n%3;
            //int num=n/3;
            n/=3;
            
            if(detect==0) n--;
            answer=numbers[detect]+answer;
        }
        
        return answer;
    }
}