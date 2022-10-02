class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int width=0;
        int height=0;
        for(int i=0;i<sizes.length;i++){
            int v=Math.max(sizes[i][0],sizes[i][1]);  //한쪽은 제일 길게, 한쪽은 제일 작게 걍 탐색만 하면 됨
            int h=Math.min(sizes[i][0],sizes[i][1]);  //가로길이에 전부 다 긴부분 놓고 세로부분에 다 작은부분으로 놓기
            width=Math.max(width,v);
            height=Math.max(height,h);
        }
        return answer=width*height;
    
    }
}