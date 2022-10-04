import java.util.ArrayList;
class Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> al=new ArrayList<>();
        int[] arr1={1,2,3,4,5};
        int[] arr2={2,1,2,3,2,4,2,5};
        int[] arr3={3,3,1,1,2,2,4,4,5,5};
        int[] answerCount={0,0,0};
        
        for(int i=0;i<answers.length;i++){
            if(arr1[i%5]==answers[i]) answerCount[0]++;
            if(arr2[i%8]==answers[i]) answerCount[1]++;
            if(arr3[i%10]==answers[i]) answerCount[2]++;
        }
        int max=answerCount[0];
        int size=0;
        for(int i=1;i<answerCount.length;i++){
            if(max<answerCount[i]){
                max=answerCount[i];
            }
        }
        
        
        for(int i=0;i<answerCount.length;i++){
            if(answerCount[i]==max){
                al.add(i+1);
            }
        }
        int[] answer = new int[al.size()];
        for(int i=0;i<al.size();i++){
            answer[i]=al.get(i);
        }
        
        
        
        return answer;
    }
}