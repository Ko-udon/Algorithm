class Solution {
    public int check(int n){
        switch(n){
            case 6:
                return 1;
                
            case 5:
                return 2;
                
            case 4:
                return 3;
                
            case 3:
                return 4;
                
            case 2:
                return 5;
               
            default:
                return 6;
                
                
        }
    }
    public int[] solution(int[] lottos, int[] win_nums) {
        
        int correctCount=0;
        int zeroCount=0;
        for(int i : lottos){
            for(int j:win_nums){
                if(i==j){
                    correctCount++;
                }
            }
            if(i==0){
                zeroCount++;
            }
        }
        int min=correctCount;
        int max=correctCount+zeroCount;
        
        int[] answer = {check(max),check(min)};
        return answer;
    }
}