class Solution {
    public String solution(int n) {
        String answer = "";
        boolean tmp=true;
        while(n>0){
            if(tmp==true){
                answer+="수";
                tmp=false;
            }
            else{
                answer+="박";
                tmp=true;
            }
            n--;
        }
        return answer;
    }
}