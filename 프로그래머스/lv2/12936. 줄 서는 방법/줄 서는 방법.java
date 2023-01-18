import java.util.ArrayList;
import java.util.List;
class Solution {
    public int[] solution(int n, long k) {
        int[] answer = new int[n];
        List<Integer> list = new ArrayList<>();

        long total = 1;
        for(int i=1;i<=n;i++){
          list.add(i);
          total*=i;
        }

        //배열은 0부터 시작
        k--;

        //첫번째수, n=4 가정, k=15라고 할때
        // 전체 개수 / 요소 개수 = 24 / 4 = 6
        // k / 6 = 14 % 6  = 2
        //2는 배열에서 [1,2,3,4] -> 3

        //요소 1개를 구했으니 구할 번호 k는 위에서 구한 6만큼 제외
        //14 % 6 = 2 = k

        // 두번째수
        // 3!=6
        // 6 / 3 = 2
        // 다음 2 / 2 % 2.xxx / 2 = 1
        // -> 2

        // 세번째수
        // 2/2 = 1
        // 1/1 = 1

        int idx=0;
        while (idx<n){
          total/=n - idx;
          answer[idx++] = list.remove((int) (k/total));
          k%=total;
        }
        // n=4 -> 24

        return answer;
    }
}