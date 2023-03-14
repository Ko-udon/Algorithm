class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        boolean[][] game = new boolean[n][n];

        //results에 나온 결과를 토대로 boolean값 업데이트
        for (int i = 0; i < results.length; i++) {
            game[results[i][0] - 1][results[i][1] - 1] = true;
        }

        // a>b 이고 b>c 이면 a>c이다 형식의 코드
        //삼중for문이라 효율성은 좀 애매하다,,
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (game[j][i] && game[i][k]) {
                        game[j][k] = true;
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            int result = 0;
            for (int j = 0; j < n; j++) {
                if (game[i][j] || game[j][i]) {
                    result++;
                }
            }
            //선수 한명이 다른 모든 선수와 승부 결과가 존재하는 경우
            if (result == n - 1) {
                answer++;
            }
        }

        return answer;
    }
}