import java.util.*;
class Solution {
    public int solution(String dirs) {
        int answer = 0;
        int x=0;
        int y=0;
        List<String> list=new ArrayList<>();
        for(int i=0;i<dirs.length();i++){
            char c=dirs.charAt(i);
            String pos=Integer.toString(x)+Integer.toString(y);
            switch (c){
                case 'U':
                    y++;
                    break;
                case 'D':
                    y--;
                    break;
                case 'R':
                    x++;
                    break;
                case 'L':
                    x--;
                    break;
                default:
                    break;
            }

            if(x<-5){
                x=-5;
                continue;
            }else if(x>5){
                x=5;
                continue;
            }else if(y<-5){
                y=-5;
                continue;
            }else if(y>5){
                y=5;
                continue;
            }



                String to=Integer.toString(x)+Integer.toString(y);
                String posToGo=pos+to;
                String goToPos=to+pos;

                if(!list.contains(posToGo)&&!list.contains(goToPos)){
                    list.add(posToGo);
                    list.add(goToPos);
                    answer++;
                }




        }

        System.out.println(answer);
        return answer;
    }
}