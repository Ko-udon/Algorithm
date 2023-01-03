import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;

    //전체 반복은 discount크기만큼의 -10 까지
    for(int i=0;i<=discount.length-10;i++){
      String[] tmp= Arrays.copyOfRange(discount,i,i+10);
      Map<String,Integer> map=new HashMap<>();
      for(int j=0;j<want.length;j++){
        map.put(want[j],number[j]);
      }

      //map안에 원하는 재료가 tmp배열에 있으면 값을 -1 한 후 바로 break;
      //break하지 않으면 해당 값을 계속 감소시킴
      for(int k=0;k<tmp.length;k++){
        for(String key : map.keySet()){
          if(tmp[k].equals(key)){
            map.put(key,map.get(key)-1);
            break;
          }
        }
      }

      //map의 value가 전부 0이면 answer++
      boolean isAllZero=true;
      for(String key : map.keySet()){
        if(map.get(key)!=0){
          isAllZero=false;
          break;
        }
      }
      if (isAllZero){
        answer++;
      }
    }
    
    
    return answer;
    }
}