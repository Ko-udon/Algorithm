class Solution {
    public long solution(long n) {
        long answer = 0;
        double tmp=0;
        tmp=Math.sqrt(n);
        if (tmp%1>0) {
        	answer = -1;
        }
        else {
            answer = (long) Math.pow(tmp+1, 2);
        }
        return answer;
    }
}