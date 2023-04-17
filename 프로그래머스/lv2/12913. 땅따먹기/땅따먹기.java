import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
class Solution {
    int solution(int[][] land) {

        int answer = 0;
        for(int i=1;i<land.length;i++){
            //각 행별 같은 열의 값을 제외하고 최대값에 더한값으로 업데이트 해준다.
            land[i][0]+=Math.max(land[i-1][1], Math.max(land[i-1][2],land[i-1][3])); 
            land[i][1]+=Math.max(land[i-1][0], Math.max(land[i-1][2],land[i-1][3]));
            land[i][2]+=Math.max(land[i-1][0], Math.max(land[i-1][1],land[i-1][3]));
            land[i][3]+=Math.max(land[i-1][0], Math.max(land[i-1][1],land[i-1][2]));
        }

        for(int i=0;i<4;i++){
            answer=Math.max(answer,land[land.length-1][i]);
        }

        return answer;

    }
}