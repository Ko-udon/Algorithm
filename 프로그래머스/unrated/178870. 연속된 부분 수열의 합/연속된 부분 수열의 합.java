class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = new int[2];
        int left = 0;
        int right = 0;
        int value = sequence[left];
        
        //0번 인덱스가 k값인 경우
        if(sequence[0] == k){
            return answer;
        }
        
        while((right < sequence.length - 1) && (right < sequence.length - 1)){
            while((right <= sequence.length -1) && (value < k)){
                value+=sequence[++right];
            }
            
            while((left <= sequence.length -1) && (value > k)){
                value-=sequence[left++];
            }
            
         
            
            //길이가 짧으면서 앞쪽에 나오는 수열이여야 한다
            while(value == k){
                //처음 찾은 경우
                if((answer[0] == 0) && (answer[1] == 0)){
                    answer[0] = left;
                    answer[1] = right;
                }else{ //처음 찾은 경우가 아니라면 길이가 더 짧은지, 앞쪽인지 비교
                    if(answer[1] - answer[0] > right - left){
                        answer[0] = left;
                        answer[1] = right;
                    }
                }
                
                //while문을 탈출해서 계속 찾기
                value-=sequence[left++];
            }
            
        }
        
        
        return answer;
    }
}