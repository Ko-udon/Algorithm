import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer=new int[commands.length];
        for(int y=0;y<commands.length;y++){
            int[] arr=Arrays.copyOfRange(array, commands[y][0]-1, commands[y][1]);
            //System.out.println(Arrays.toString(arr));
            Arrays.sort(arr);
            answer[y]=arr[commands[y][2]-1];

        }
        
       
        return answer;
    }
}