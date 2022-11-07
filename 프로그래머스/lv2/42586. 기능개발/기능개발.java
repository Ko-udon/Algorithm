import java.util.ArrayList;
import java.util.*;
import java.util.stream.Collectors;
class Solution {
    public List solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        List <Integer> list=new ArrayList<>();
        List <Integer> progress= Arrays.stream(progresses).boxed().collect(Collectors.toList());
        List<Integer> speed=Arrays.stream(speeds).boxed().collect(Collectors.toList());
        int days=(100-progress.get(0))%speed.get(0)==0?(100-progress.get(0))/speed.get(0):(100-progress.get(0))/speed.get(0)+1;
        

        int tmp=0;
        while(!progress.isEmpty()){
            int finishDay=(100-progress.get(0))%speed.get(0)==0?(100-progress.get(0))/speed.get(0):(100-progress.get(0))/speed.get(0)+1;
            if(finishDay<=days){
                tmp++;
            }
            else{
                list.add(tmp);
                days=finishDay;
                tmp=1;
            }
            if(progress.size()==1){
                list.add(tmp);
            }
            System.out.println(progress.get(0));
            progress.remove(progress.get(0));
            speed.remove(speed.get(0));
        }
        return list;
    }
}