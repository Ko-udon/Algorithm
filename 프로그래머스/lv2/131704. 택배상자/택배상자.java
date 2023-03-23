import java.util.*;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
      
        Stack<Integer> subContainer = new Stack<>();
        
        int next = 1;  //상자순서
        int pos = 0;  //order 순서 체크
        
        while(true){
            
            
            //보조 컨테이너 벨트에 값이 있고 그 다음 값이 상자 순서와 일치하는 경우
            if((!subContainer.isEmpty()) && (order[pos] == subContainer.peek())){
                answer++;
                pos++;
                subContainer.pop();
                
                continue;
            }
            
            
            //더이상 불가능한 경우 반복 탈출
            if(next > order.length){
                break;
            }
            
            
            
            //상자 순서와 다음 상자가 일치하는 경우
            if(order[pos] == next){
                answer++;
                
                pos++;
                next++;
                
                continue;
                
            }
            
            subContainer.push(next);
            next++;
            
        }
        
        
        return answer;
    }
}