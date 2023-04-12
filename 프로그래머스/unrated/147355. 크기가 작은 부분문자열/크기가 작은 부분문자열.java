class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int size = p.length();
        
        Long pN = Long.parseLong(p);
        for(int i =0; i<=t.length() - size; i++){
            Long n = Long.parseLong(t.substring(i,i+size));
            if(n<=pN){
                answer++;
            }
        }
        return answer;
    }
}