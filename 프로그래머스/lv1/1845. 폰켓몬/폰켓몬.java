import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int N=nums.length;
        HashSet<Integer> set=new HashSet<>();
        for(int i=0;i<N;i++){
            set.add(nums[i]);
        }
        if(N/2<set.size()){
            return N/2;
        }
        else{
            return set.size();
        }
        //return answer;
    }
}