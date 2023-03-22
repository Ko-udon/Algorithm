import java.util.*;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        
        //col 컬럼의 값을 기준으로 오름차순 정렬
        Arrays.sort(data,(o1, o2)->{
            //만약 값이 같다면, 기본키(첫번째)를 기준으로
            if(o1[col-1] == o2[col-1]){
                return o2[0] - o1[0];
            }
            
            return o1[col-1] - o2[col-1]; 
        });
        
        //bitwise XOR
        for(int i = row_begin - 1; i < row_end; i++){
            int mod = 0;
            for(int tmp : data[i]){
                mod += tmp % (i+1);
            }
            
            answer ^= mod;
        }
        
        return answer;
    }
}