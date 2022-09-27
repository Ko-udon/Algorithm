class Solution {
    public String solution(String s) {
        String answer = "";
        char[] charr=new char[s.length()];
        for(int i=0;i<s.length();i++){
            charr[i]=s.charAt(i);
        }
        
        for(int i=0;i<charr.length;i++){
            for(int j=i;j<charr.length;j++){
                if(charr[i]<charr[j]){
                    char c=charr[i];
                    charr[i]=charr[j];
                    charr[j]=c;
                }
            }
        }
        for(int i=0;i<charr.length;i++){
            answer+=charr[i];
        }
        return answer;
    }
}