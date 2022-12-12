class Solution {
    public String solution(int n, int t, int m, int p) {
        String answer = "";

        int countAnswer=0;
        int num=0;
        String toAnswer="";
        while(toAnswer.length()<m*t){
            toAnswer+=(Integer.toString(num++,n));
        }
        //System.out.println(toAnswer);

        for(int i=p-1;i<m*t;i=i+m){
            answer+=toAnswer.charAt(i);
        }
        return answer.toString().toUpperCase();
    }
}