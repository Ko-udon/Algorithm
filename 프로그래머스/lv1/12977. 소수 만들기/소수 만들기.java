
class Solution {
    public boolean prime(int n){
        for(int i=2; i*i<=n; i++){
            if(n % i == 0){
            return false;
            }
        }
        return true;
    }
    
    public int solution(int[] nums) {
        int answer = 0;
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                for(int k=j+1;k<nums.length;k++){
                    int tmp=nums[i]+nums[j]+nums[k];
                    if(prime(tmp)==true){
                        answer++;
                    }    
                }
            }
        }

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        //System.out.println("Hello Java");

        return answer;
    }
}