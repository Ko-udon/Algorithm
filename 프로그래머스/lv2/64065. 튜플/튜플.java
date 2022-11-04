import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public ArrayList solution(String s) {
        ArrayList<Integer> answer=new ArrayList<>();
        s=s.substring(2,s.length());
        s=s.substring(0,s.length()-2);
        s=s.replace("},{"," ");

        String[] str=s.split(" ");
        Arrays.sort(str, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return Integer.compare(o1.length(),o2.length());
            }
        });

        for(String K:str){
            String[] tmp=K.split(",");
            for(int i=0;i<tmp.length;i++){
                int n=Integer.parseInt(tmp[i]);
                if(!answer.contains(n)) answer.add(n);
            }
        }
        return answer;
    }
}