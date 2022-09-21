class Solution {
    public static int convertNum(int x){
        int n=0;

        while(x>0){
            n+=x%10;
            x/=10;
        }

        return n;
    }
    
    public boolean solution(int x) {
        boolean answer = true;
        int n=convertNum(x);
        answer=x%n==0?true:false;
        return answer;
    }
}