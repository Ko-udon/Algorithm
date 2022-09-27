class Solution {
    public int yaksu(int n){
        int tmp=0;
        for(int i=1;i<=n;i++){
            if(n%i==0){
                tmp++;
            }
        }
        //System.out.println(tmp);
        return tmp;
    }
    public int solution(int left, int right) {
        int answer = 0;
        for(int i=left;i<=right;i++){
            answer=(yaksu(i)%2==0)?answer+i:answer-i;
        }
        
        return answer;
    }
}