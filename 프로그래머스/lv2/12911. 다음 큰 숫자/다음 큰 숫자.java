class Solution {
    public int solution(int n) {
        int answer = 0;
        int countOne=0;
        String binary=Integer.toBinaryString(n);
            for(int j=0;j<binary.length();j++){
                char c=binary.charAt(j);
                if(c=='1'){
                    countOne++;
                }
            }
        int i=n+1;
        while(true){
            
            int countOne2=0;
            binary=Integer.toBinaryString(i);
            for(int j=0;j<binary.length();j++){
                char c=binary.charAt(j);
                if(c=='1'){
                    countOne2++;
                }
            }
            if(countOne==countOne2){
                return i;
            }
            else{
                i++;
            }
        }
    }
}