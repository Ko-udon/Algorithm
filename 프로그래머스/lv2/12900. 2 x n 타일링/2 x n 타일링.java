class Solution {
    public int solution(int n) {
        int answer=0;
        int t=1;
        int u=1;
        for(int k=2;k<=n;k++){
          answer=(t+u)%1000000007;
          t=u;
          u=answer;
        }


        return answer;
    }
}