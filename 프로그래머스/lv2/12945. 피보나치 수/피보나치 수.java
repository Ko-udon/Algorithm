class Solution {
    public int solution(int n) {
        int answer = 0;
        int a1 = 1;
        int a2 = 1;        
        for(int i=3; i<=n; i++){
            answer=(a1+a2)%1234567;
            a1=a2;
            a2=answer;
        }
        return answer;
    }
}