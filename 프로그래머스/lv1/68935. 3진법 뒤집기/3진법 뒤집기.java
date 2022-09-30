import java.util.Stack;
class Solution {
    public int solution(int n) {
        int answer = 0;
        int tmp=n;
        Stack<Integer> stack=new Stack<>();
        while(tmp!=0){  //3진법 전환
            stack.push(tmp%3);
            tmp=tmp/3;   
        }
        
        tmp=1;     
        int size=stack.size();
        for(int i=0;i<size;i++){
            answer+=tmp*stack.pop();
            tmp=tmp*3;  
        }
        
        return answer;
    }
}