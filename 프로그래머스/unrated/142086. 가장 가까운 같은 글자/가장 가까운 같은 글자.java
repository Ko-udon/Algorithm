class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        answer[0] = -1;
        int left = 0;
        int right = 1;
        
        while(right < s.length()){
            char c = s.charAt(right);
            answer[right] = -1;
            left = right - 1;
            while(left >= 0){
                char c2 = s.charAt(left);
                if(c2 == c){
                    answer[right] = right - left;
                    break;
                }
                left--;
            }
            right++;
            
        }
        return answer;
    }
}