class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        int tmp=0;
        for(String i:seoul){
            if(i.equals("Kim")){
                answer="김서방은 "+tmp+"에 있다";
                break;   
            }
            tmp++;
        }

        return answer;
    }
}