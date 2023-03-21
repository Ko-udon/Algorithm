class Solution {
    private static final int MAX = Integer.MAX_VALUE;
    
    public int solution(int x, int y, int n) {
        int answer = 0;
        int[] check = new int[y+1];
        
        for(int i = x+1; i<y+1; i++){
            int caseA = MAX, caseB = MAX, caseC = MAX, tmp;
            
            if(isLow(x,(i-n))){
                caseA = check[i - n];
            }
            
            if(isDivided(i,2) && isLow(x, i/2)){
                caseB = check[i/2];
            }
            
            if(isDivided(i,3) && isLow(x, i/3)){
                caseC = check[i/3];
            }
            
            tmp = Math.min(caseB, caseC);
            tmp = Math.min(tmp , caseA);
            
            
            check[i] = tmp < MAX?tmp+1:MAX;
            
        }
        
        
        answer = check[y] < MAX?check[y]:-1;
        
        return answer;
    }
    
    //x보다 작은 수들은 체크하지 않기 
    private static boolean isLow(int x, int tmp){
        return (x <= tmp);
    }
    
    //2, 3으로 나누었을때 딱 나누어 떨어지는지 확인
    private static boolean isDivided(int x, int i){
        if((x/i > 0) && (x%i == 0)){
            return true;
        }
        return false;
    }
    
    
}