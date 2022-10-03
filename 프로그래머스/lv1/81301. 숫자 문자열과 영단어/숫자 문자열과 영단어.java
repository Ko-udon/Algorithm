import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] digitArr={"zero","one","two","three","four","five","six","seven","eight","nine","ten"};
        boolean isWord=false;
        ArrayList<Character> arrList=new ArrayList<>();
        String S="";
        ArrayList<String> answerList=new ArrayList<>();
        for(int i=0;i<s.length();i++){
            if(Character.isDigit(s.charAt(i))){    
                answerList.add(Character.toString(s.charAt(i)));
                
            }
            else{
                S+=s.charAt(i);
                if(Arrays.asList(digitArr).contains(S)){
                    answerList.add(Integer.toString(Arrays.asList(digitArr).indexOf(S)));
                    S="";
                }   
            }
        }
        int ten=1;
        for(int i=answerList.size()-1;i>-1;i--){
            answer+=ten*Integer.parseInt(answerList.get(i));
            ten*=10;
        }
        
        return answer;
    }
}