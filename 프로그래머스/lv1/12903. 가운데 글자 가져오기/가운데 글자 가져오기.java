class Solution {
    public String solution(String s) {
        String answer = "";
        int size=s.length();
        
        answer=(size%2==0)? Character.toString(s.charAt(size/2-1))+Character.toString(s.charAt(size/2)):Character.toString(s.charAt(size/2));
        
        return answer;
    }
}