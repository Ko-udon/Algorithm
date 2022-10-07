class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int Llen=0;
        int Rlen=0;
        int[] left={0,0};
        int[] right={2,0};
        int[][] keypad={{1,0},{0,3},{1,3},{2,3},{0,2},{1,2},{2,2},{0,1},{1,1},{2,1}};
        
        for(int i=0;i<numbers.length;i++){
            int[] target=keypad[numbers[i]];
            if(target[0]==0){
                answer+="L";
                left=target;
            }
            else if(target[0]==2){
                answer+="R";
                right=target;
            }
            else{
                Llen=Math.abs(target[0]-left[0])+Math.abs(target[1]-left[1]);
                Rlen=Math.abs(target[0]-right[0])+Math.abs(target[1]-right[1]);
                if(Llen<Rlen){
                    answer+="L";
                    left=target;
                }
                else if(Llen>Rlen){
                    answer+="R";
                    right=target;
                }
                else{
                    if(hand.equals("left")){
                        answer+="L";
                        left=target;
                    }
                    else{
                        answer+="R";
                        right=target;
                    }
                }
            }
            
            
        }
        
        
        return answer;
    }
}