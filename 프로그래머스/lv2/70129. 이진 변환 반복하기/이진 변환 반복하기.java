class Solution {
    public int[] solution(String s) {
        
        int countTurn=0;
        int countZero=0;
        while(!s.equals("1")){
            String s2="";
            for(int i=0;i<s.length();i++){
                if(s.charAt(i)!='0'){
                    s2+=Character.toString(s.charAt(i));
                }
                else{
                    countZero++;
                }
            }
            
            s=Integer.toString(s2.length(),2);
            System.out.println(s);
            countTurn++;
        }
        int[] answer = {countTurn,countZero};
        return answer;
    }
}