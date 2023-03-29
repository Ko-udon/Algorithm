class Solution {
    public int[] solution(String[] wallpaper) {
        int[] answer = new int[4];
        
        int lux = wallpaper.length;
        int luy = wallpaper[0].length();
        int rdx = 0;
        int rdy = 0;
        
        for(int i = 0; i < wallpaper.length; i++){
            String s = wallpaper[i];
            if(!s.contains("#")){
                continue;
            }
            
            int x = i;
            int y = s.indexOf("#");
            
            lux = Math.min(x,lux);
            luy = Math.min(y,luy);
            rdx = Math.max(x,rdx);
            rdy = Math.max(y,rdy);
            
            y = s.lastIndexOf("#");
            rdx = Math.max(x,rdx);
            rdy = Math.max(y,rdy);
            
        }
        
        answer[0] = lux;
        answer[1] = luy;
        answer[2] = ++rdx;
        answer[3] = ++rdy;
        
        
        return answer;
    }
}