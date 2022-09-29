class Solution {
    public String solution(String s) {
        String answer = "";
        int cnt=0;
        String[] arr=s.split("");
        for(String ss:arr){
            if(ss.contains(" ")){
                cnt=0;
            }
            else{
                cnt++;
            }
            
            if(cnt%2==0){
                answer+=ss.toLowerCase();
            }
            else{
                answer+=ss.toUpperCase();
            }
        }
        return answer;
    }
}