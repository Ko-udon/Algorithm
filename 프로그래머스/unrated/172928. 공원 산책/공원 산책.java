class Solution {
    public int[] solution(String[] park, String[] routes) {
        int[] answer = new int[2];
        int x = 0, y = 0;
        int H = park.length;
        int W = park[0].length();
        
        //시작점 찾기
        for(int i = 0; i<park.length; i++){
            if(park[i].contains("S")){
                x = i;
                y = park[i].indexOf("S");
            }
        }
        
        
        for(String commands : routes){
            String[] command = commands.split(" ");
            String dir = command[0];
            int value = Integer.parseInt(command[1]);
            
            switch(dir){
                case "E":
                    if(check(dir,x,y,x,y+value,H,W,park)){
                        y+=value;
                    }
                    break;
                    
                case "W":
                    if(check(dir,x,y,x,y-value,H,W,park)){
                        y-=value;
                    }
                    break;
                case "S":
                    if(check(dir,x,y,x+value,y,H,W,park)){
                        x+=value;
                    }
                    break;
                case "N":
                    if(check(dir,x,y,x-value,y,H,W,park)){
                        x-=value;
                    }
                    break;
                default:
                    break;
            }
            
        }
        
        answer[0] = x;
        answer[1] = y;
        
        
        return answer;
    }
    
    boolean check(String dir, int startX, int startY, int toX, int toY, int H, int W, String[] park){
        int len = 0;
        
        switch(dir){
                case "E":
                    if((toY) >= W){
                        return false;
                    } 
                
                    for(int i = startY; i < toY+1; i++){
                        if(park[startX].charAt(i) == 'X'){
                            return false;
                        }
                    }
                    break;
                
                case "W":
                    if((toY) < 0){
                        return false;
                    } 
                
                    for(int i = toY; i < startY; i++){
                        if(park[startX].charAt(i) == 'X'){
                            return false;
                        }
                    }
                    break;
                
                case "S":
                    if((toX) >= H){
                        return false;
                    } 
                
                    for(int i = startX; i < toX+1; i++){       
                        if(park[i].charAt(startY) == 'X'){
                            return false;
                        }
                    }
                    break;
                
                case "N":
                    if((toX) < 0){
                        return false;
                    } 
                
                    for(int i = toX; i < startX+1; i++){
                        if(park[i].charAt(startY) == 'X'){
                            return false;
                        }
                    }
                    break;
                
                default:
                    break;
            }
        
        return true;
        
    }
    
}