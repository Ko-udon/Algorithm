class Solution {
    public int[] solution(int n) {
        int[] answer = new int[(n * (n + 1)) / 2];
        int[][] matrix = new int[n][n];

        int x = -1, y = 0;
        int num = 1;

        for (int i = 0; i < n; i++) {  //열
          for (int j = i; j < n; j++) {  //행
            if (i % 3 == 0) { //아래로 이동
              x++;
            } else if (i % 3 == 1) {  //오른쪽으로 이동
              y++;
            } else if (i % 3 == 2) {  //대각선 왼쪽 위로 이동
              x--;
              y--;
            }
            matrix[x][y] = num++;
          }
        }

        int k = 0;
        for (int i = 0; i < n; i++) {
          for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
              break;
            }
            answer[k++] = matrix[i][j];
          }
        }
        return answer;
    }
}