class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        if(a==b) return answer=a;
        else{
            while(a!=b){
                if(a<b){
                    answer+=a;
                    a++;
                }
                else{
                    answer+=a;
                    a--;
                }
            }  
            answer+=b;
        }
        return answer;
    }
}